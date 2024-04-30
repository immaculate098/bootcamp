from django import forms
from .models import Sitter

class SitterForm(forms.ModelForm):
    on_duty = forms.BooleanField(label='On Duty', required=False)
    off_duty = forms.BooleanField(label='off Duty', required=False)

    class Meta:
        model = Sitter
        fields = ['name', 'gender', 'on_duty','off_duty']
