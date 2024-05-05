
from django.db import models


class Sitter(models.Model):
    name = models.CharField(max_length=100)
    babies_attended = models.IntegerField(default=0) 


    def __str__(self):
        return self.name

class Payment(models.Model):
    sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    payment_type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    babies_attended = models.IntegerField(default=0) 


    def __str__(self):
        return f"{self.sitter.name} - {self.payment_date}"

