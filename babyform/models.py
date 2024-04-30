from django.db import models
from django.utils import timezone

class Sitter(models.Model):
    name = models.CharField(max_length=100)
    is_on_duty = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Baby(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    brought_by = models.CharField(max_length=100, default="")
    arrival_time = models.DateTimeField(default=timezone.now)
    parents_names = models.CharField(max_length=200, null=True)
    fee = models.CharField(max_length=20, default='UGX 0') 
    period_of_stay = models.CharField(max_length=100)
    baby_number = models.IntegerField(default='')

    assigned_sitter = models.ForeignKey(Sitter, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
