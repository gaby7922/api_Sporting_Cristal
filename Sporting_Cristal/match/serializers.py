from rest_framework import serializers
from match.models import Torneo

# Serializers que formatea la data para ser enviada a travez del webservice
class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        exclude = ('id',)
