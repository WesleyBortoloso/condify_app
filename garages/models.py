from django.db import models

class Garage(models.Model):
    number = models.IntegerField()
    reserved = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
