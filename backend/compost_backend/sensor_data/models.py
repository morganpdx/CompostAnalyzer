from __future__ import unicode_literals

from django.db import models
from compost_backend.compost_sensor.models import CompostSensor

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now = True)
    value = models.FloatField()
    sensor = models.ForeignKey(
        CompostSensor,
        on_delete=models.CASCADE,
        verbose_name="the compost sensor that generated this data",
        null=True
    )


    def __str__(self):
        return self.id