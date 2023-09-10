from django.db import models

class Resident(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    apartment = models.CharField(max_length=4)