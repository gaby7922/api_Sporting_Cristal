import json
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework import viewsets, status
from rest_framework.response import Response
from match.models import Torneo
from match.serializers import TorneoSerializer

#creacion de las clase que muestra informacion 

class MatchApi(APIView):

    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        queryset = Torneo.objects.all()
        serializer = TorneoSerializer(queryset, many=True)
        return Response(serializer.data)
        
# creacion de clase que lee y guarda la informacion

class SaveData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        respuesta = requests.get('http://sporting.backend.masfanatico.cl/api/match/in_competition/?competition=torneo-descentralizado&format=json')
        data = json.loads(respuesta.text)
        data = data['matchs']
        respuesta_tarea = []
        for o in data:
            v = {
                'uuid': o['uuid'],
                'referee': o['referee'],
                'local_goals': o['local_goals'],
                'date': o['date'],
                'alineaciones': o['alineaciones'],
                'city_reference_a': o['city_reference_a'],
                'city_reference_b': o['city_reference_b'],
                'heatmap': o['heatmap'],
                'id_opta': o['id_opta'],
                'image_streaming': o['image_streaming'],
                'minute': o['minute'],
                'slug': o['slug'],
                'stage': o['stage'],
                'status': o['status'],
                'time': o['time'],
                'timestamp': o['timestamp'],
                'visit_goals': o['visit_goals'],
                'weather': o['weather'],
            }
            respuesta_tarea.append(v)
            obj = Torneo.objects.get_or_create(**v)
        return Response(respuesta_tarea)
                