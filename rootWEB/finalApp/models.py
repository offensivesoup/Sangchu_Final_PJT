from django.db import models

class Views(models.Model):
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.views)


# Create your models here.
