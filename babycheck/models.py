from django.db import models
from django.utils import timezone


class Baby(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BabyDeparture(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True)
    baby_fetcher = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"Departure of {self.baby.name}"

