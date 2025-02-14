# models.py
from django.db import models

class Account(models.Model):
    ACCOUNT_TYPES = (
        ('SAVINGS', 'Savings'),
        ('CURRENT', 'Current'),
    )
    
    account_number = models.CharField(max_length=20, unique=True)
    account_holder = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.account_holder} - {self.account_number}"