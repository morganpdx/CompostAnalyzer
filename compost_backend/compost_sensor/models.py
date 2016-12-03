from __future__ import unicode_literals

from django.db import models

class CompostSensor(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    timestamp = models.DateTimeField(auto_now = True)
    value = models.FloatField()

    def __str__(self):
        return self.name