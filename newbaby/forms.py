from django import forms
from .models import BabyArrival  

class BabyArrivalForm(forms.ModelForm):  
    class Meta:
        model = BabyArrival  
        fields = ['baby_name', 'baby_deliverer', 'time_in', 'comment']  
