from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Sitter(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    nin = models.CharField(max_length=15)
    religion = models.CharField(max_length=50, blank=True)
    education = models.CharField(max_length=100)
    contact = models.CharField(max_length=15, default='')
    sitter_number = models.CharField(max_length=100)
    next_of_kin = models.CharField(max_length=100)
    recommender_name = models.CharField(max_length=100)
    recommender_contact = models.CharField(max_length=15, default='') 