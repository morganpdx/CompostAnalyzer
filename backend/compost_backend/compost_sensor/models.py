from __future__ import unicode_literals

from django.db import models
from compost_backend.compost_bin.models import CompostBin
from compost_backend.sensor_data.models import SensorData

class CompostSensor(models.Model):
    SENSOR_TYPES = (
        ('temp', 'Temperature'),
        ('hum', 'Humidity'),
        ('vib', 'Vibration')
    )
    type = models.CharField(max_length=1, choices=SENSOR_TYPES)
    bin = models.ForeignKey(
        CompostBin,
        on_delete=models.CASCADE,
        verbose_name="the compost bin this sensor is in",
        null=True
    )

    def __str__(self):
        return self.type + ' sensor'

    def add_data(self, sensor_values):
        """
        Save an array of values to the sensor
        """
        for d in sensor_values:
            SensorData.object.create(
                sensor = self,
                data = d
            )