from django.db import models

class Sitter(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Baby(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed

