from django.db import models

class Apartment(models.Model):
    number = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    description = models.CharField(max_length=100)
