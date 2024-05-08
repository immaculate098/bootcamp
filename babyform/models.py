from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import re

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
    


class Sitter(models.Model):
    name = models.CharField(max_length=100)
    on_duty = models.BooleanField(default=False)
    attendancestatus=models.CharField(choices=[('on_duty', 'on_duty')],max_length=100,default='on_duty')
    

    def __str__(self):
        return self.name



class Baby(models.Model):
     GENDER_CHOICES = (
         ('male', 'Male'),
        ('female', 'Female'),
     )

     name = models.CharField(max_length=100, validators=[validate_letters])
     gender = models.CharField(max_length=10,choices=GENDER_CHOICES,default='male')
     age = models.IntegerField(validators=[validate_numbers])
     location = models.CharField(max_length=100, validators=[validate_letters])
     brought_by = models.CharField(max_length=100, default="", validators=[validate_letters])
     arrival_time = models.DateTimeField(default=timezone.now)
     parents_names = models.CharField(max_length=200, null=True, validators=[validate_letters])
     fee = models.CharField(max_length=20, default='UGX 0', validators=[validate_numbers])
     period_of_stay = models.CharField(max_length=100, validators=[validate_letters])
     baby_number = models.CharField(max_length=500, unique=True, null=True,blank=False)
     assigned_to=models.ForeignKey(Sitter,on_delete=models.CASCADE, null=True, blank=False,)


     def __str__(self):
        return self.name
