from django import forms

class VerificationForm(forms.Form):
    code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter 6-digit code'}))
