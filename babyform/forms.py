from django import forms
from .models import Baby

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ['baby_name', 'gender', 'age', 'location', 'brought_by', 'arrival_time', 'parents_names', 'baby_number', 'assigned_to']
        