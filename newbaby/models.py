from django.db import models
from django.utils import timezone

class BabyArrival(models.Model):
    baby_name = models.CharField(max_length=100)
    baby_deliverer = models.CharField(max_length=100)
    time_in = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True)
