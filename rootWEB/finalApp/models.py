from django.db import models
from django.contrib.auth.models import User


class Views(models.Model):
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.views)



