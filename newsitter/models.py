
from django.db import models

class Payment(models.Model):
    PAYMENT_TYPES = (
        ('halfday', 'Half Day'),
        ('fullday', 'Full Day'),
        ('monthlypay', 'Monthly Payment'),
    )

    baby_name = models.CharField(max_length=100 , default='')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    payment_type = models.CharField(max_length=20, default='pay', choices=PAYMENT_TYPES)
    change_received = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
