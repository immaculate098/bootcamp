from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
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


class Student(models.Model):
    name = models.CharField(max_length=100, validators=[validate_letters])
    gender = models.CharField(max_length=10, validators=[validate_letters])
    location = models.CharField(max_length=100, validators=[validate_letters])
    date_of_birth = models.DateField()
    nin = models.CharField(max_length=14,validators=[validate_NIN_length])
    religion = models.CharField(max_length=50, blank=True,null=True,verbose_name="Religion(optional)")
    education = models.CharField(max_length=100, validators=[validate_letters])
    contact = models.CharField(max_length=15, default='',validators=[validate_contact_length])
    sitter_number = models.CharField(max_length=200,unique=True,blank=False, null=True)
    next_of_kin = models.CharField(max_length=100, validators=[validate_letters])
    recommender_name = models.CharField(max_length=100, validators=[validate_letters])
    recommender_contact = models.CharField(max_length=15, default='',validators=[validate_contact_length]) 


    def __str__(self):
        return f'Student:{self.name} {self.gender} {self.location} {self.date_of_birth} {self.nin} {self.religion} {self.education} {self.contact} {self.sitter_number} {self.next_of_kin} {self.recommender_name} {self.recommender_contact} '

