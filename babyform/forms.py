from django import forms
from .models import Baby


class BabyForm(forms.ModelForm):
         class Meta:
            model = Baby
            fields = '__all__'
            widgets = {
            'fee': forms.NumberInput(attrs={'type': 'number'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
        }
