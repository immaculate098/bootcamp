from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import re
from sitterlist.models import Student

def validate_letters(value):
    if not re.match("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")

def validate_numbers(value):
    if not re.match("^[0-9]*$", str(value)):
        raise ValidationError("Only numbers are allowed.")



def validate_contact_length(value):
    if len(value) != 10:
        raise ValidationError("Contact field must contain exactly 10 digits.")

def validate_NIN_length(value):
    if len(value) != 14:
        raise ValidationError("NIN field must contain exactly 14 digits.")
    

class Student(models.Model):
    name = models.CharField(max_length=100, validators=[validate_letters])
    def __str__(self):
        return self.name

class Baby(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    baby_name = models.CharField(max_length=100, validators=[validate_letters], null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    age = models.IntegerField(validators=[validate_numbers])
    location = models.CharField(max_length=100, validators=[validate_letters])
    brought_by = models.CharField(max_length=100, default="", validators=[validate_letters])
    arrival_time = models.DateTimeField(default=timezone.now)
    parents_names = models.CharField(max_length=200, null=True, validators=[validate_letters])
    baby_number = models.CharField(max_length=500, unique=True, null=True, blank=False)
    assigned_to = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, related_name='babies')

    def __str__(self):
        return self.baby_name

