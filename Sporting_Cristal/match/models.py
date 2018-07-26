from django.db import models
from django.utils import timezone

#Modelo de webservice

class Torneo(models.Model):
    uuid = models.CharField(max_length=40)
    referee = models.CharField(max_length=40, null=True)
    local_goals = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    alineaciones = models.CharField(max_length=100, null=True)
    city_reference_a = models.CharField(max_length=100, default='')
    city_reference_b = models.CharField(max_length=100, default='')
    heatmap = models.CharField(max_length=100, null=True)
    id_opta = models.IntegerField()
    image_streaming = models.CharField(max_length=100, null=True)
    minute = models.FloatField()
    slug = models.CharField(max_length=100)
    stage = models.CharField(max_length=100, null=True)
    status = models.IntegerField()
    time = models.TimeField()
    timestamp = models.FloatField()
    visit_goals = models.IntegerField()
    weather = models.IntegerField()
    
    def __str__(self):
        return self.uuid


    
        
        