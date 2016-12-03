from __future__ import unicode_literals

from django.db import models
from compost_backend.compost_bin.models import CompostBin

class CompostSensor(models.Model):
    type = models.CharField(max_length = 100)
    bin = models.ForeignKey(
        CompostBin,
        on_delete=models.CASCADE,
        verbose_name="the compost bin this sensor is in",
        null=True
    )

    def __str__(self):
        return self.type + ' sensor'