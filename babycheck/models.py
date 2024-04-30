from django.db import models
from django.utils import timezone

class BabyDeparture(models.Model):
    baby_name = models.CharField(max_length=100)
    baby_fetcher = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True)

