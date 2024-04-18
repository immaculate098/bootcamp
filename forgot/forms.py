
from django import forms

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    username = forms.CharField(label='Username', max_length=100)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('@gmail.com'):
            raise forms.ValidationError("Please enter a valid Gmail address.")
        return email
