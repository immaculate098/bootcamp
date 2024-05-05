# forms.py

from django import forms
from .models import Supply, Issuing

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['item', 'quantity', 'date_received', 'unit_price', 'amount_paid', 'change_received']

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        unit_price = cleaned_data.get('unit_price')
        amount_paid = cleaned_data.get('amount_paid')

        if quantity is not None and unit_price is not None and amount_paid is not None:
            total_cost = quantity * unit_price
            if amount_paid < total_cost:
                raise forms.ValidationError("Amount paid should be greater than or equal to the total cost.")
            cleaned_data['change_received'] = amount_paid - total_cost
        return cleaned_data

class IssuingForm(forms.ModelForm):
    class Meta:
        model = Issuing
        fields = ['item', 'quantity', 'date_issued']
