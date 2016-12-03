from __future__ import unicode_literals

from django.db import models
from compost_backend.compost_sensor.models import CompostSensor

class CompostType(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    compost_bins = models.ManyToManyField
    sensors = models.ManyToManyField(CompostSensor)

    def __str__(self):
        return self.name