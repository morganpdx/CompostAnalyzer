from __future__ import unicode_literals

from django.db import models
from compost_backend.compost_user.models import CompostUser

class CompostBin(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    user = models.ForeignKey(
        CompostUser,
        on_delete=models.CASCADE,
        verbose_name="the compost bin owner",
        null=True
    )

    def __str__(self):
        return self.name or ''