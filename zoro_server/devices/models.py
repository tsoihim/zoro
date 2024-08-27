from django.db import models

class NetDevice(models.Model):
    serial = models.CharField(unique=True, max_length=32)
    ip = models.CharField(null=False, max_length=15)
    priority = models.IntegerField(default=10)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial
