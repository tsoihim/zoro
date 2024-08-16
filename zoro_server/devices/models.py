from django.db import models

class SomeDevice(models.Model):
    name = models.CharField(max_length=32)
    ip = models.CharField(max_length=15)
    priority = models.IntegerField(default=0)
    last_update = models.IntegerField(default=0)
