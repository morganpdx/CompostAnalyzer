from __future__ import unicode_literals

from django.db import models
from compost_backend.compost_bin.models import CompostBin


class CompostSensor(models.Model):
    SENSOR_TYPES = (
        ('Temperature', 'Temperature'),
        ('Humidity', 'Humidity'),
        ('Vibration', 'Vibration')
    )
    type = models.CharField(max_length=1, choices=SENSOR_TYPES)
    bin = models.ForeignKey(
        CompostBin,
        on_delete=models.CASCADE,
        verbose_name="the compost bin this sensor is in",
        null=True
    )


    def __str__(self):
        return self.type + ' sensor for bin ID# ' + str(self.get_bin())


    def get_bin(self):
        return self.bin.id