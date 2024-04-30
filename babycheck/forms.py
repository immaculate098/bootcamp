from django import forms
from .models import BabyDeparture

class BabyDepartureForm(forms.ModelForm):
    class Meta:
        model = BabyDeparture
        fields = ['baby_name', 'baby_fetcher', 'time', 'comment']

