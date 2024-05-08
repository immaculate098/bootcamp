
from django import forms
from .models import Payment, Sitter


class PaymentForm(forms.ModelForm):
    sitter = forms.ModelChoiceField(queryset=Sitter.objects.all())
    payment_type = forms.ChoiceField(choices=[ ('Monthly', 'Monthly')])
    babies_attended = forms.IntegerField(label='Number of Babies Attended', min_value=1)
    amount = forms.DecimalField() 
    
    class Meta:
        model = Payment
        fields = ['sitter', 'payment_type', 'babies_attended', 'amount']

    def clean(self):
        cleaned_data = super().clean()
        sitter = cleaned_data.get('sitter')
        payment_type = cleaned_data.get('payment_type')
        babies_attended = cleaned_data.get('babies_attended')

        if sitter and babies_attended:
            if payment_type == 'Monthly':
            
                cleaned_data['amount'] = 3000 * babies_attended * 30  

        
        amount = cleaned_data.get('amount')
        if amount is None:
            raise forms.ValidationError("Amount calculation failed. Please check your input.")

        return cleaned_data
    




