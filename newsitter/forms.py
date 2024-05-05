
from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['baby_name', 'amount_paid', 'date_paid', 'payment_type', 'change_received']
