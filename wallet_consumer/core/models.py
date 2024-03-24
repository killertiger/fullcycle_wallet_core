from django.db import models

# Create your models here.
class Account(models.Model):
    account_id = models.UUIDField(primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)