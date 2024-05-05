# models.py

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Supply(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.IntegerField(null=False, blank=False, default=0)
    date_received = models.DateField()
    amount_paid = models.IntegerField(null=False, blank=False, default=0)
    change_received = models.IntegerField(null=False, blank=False, default=0)

class Issuing(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_issued = models.DateField()
