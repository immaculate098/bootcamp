
from django.db import models
from django.utils import timezone


class Baby(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Payment(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True)
    payment_type =models.CharField(choices=[('halfday', 'halfday'),('fullday', 'fullday'),('monthlyhalfday','monthlyhalfday') ,('monthlyfullfday','monthlyfullday')], max_length=100)
    date=models.DateField(default=timezone.now)
    actual_amount = models.IntegerField(default=0,choices=[(10000, '10000'),(15000, '15000'),(300000, '300000'),(450000, '450000')])
    amount_paid = models.IntegerField(default=0)
   
    def __str__(self):
        return f"Departure of {self.baby.name}" 
    def get_balance(self):
        return self.actual_amount - self.amount_paid  


