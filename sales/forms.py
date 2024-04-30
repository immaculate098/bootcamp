from django import forms
from .models import Sale, Product

class AddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class MadeSaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
