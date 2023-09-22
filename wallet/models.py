from django.db import models

class Wallet(models.Model):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)