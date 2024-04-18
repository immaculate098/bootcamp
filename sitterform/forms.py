from django import forms
from .models import Sitter

class SitterRegistrationForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = '__all__'


    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if not contact.isdigit():
            raise forms.ValidationError("Please enter a valid contact number.")
        return contact

    def clean_sitter_number(self):
        sitter_number = self.cleaned_data.get('sitter_number')
        if not sitter_number.isdigit():
            raise forms.ValidationError("Please enter a valid sitter number.")
        return sitter_number

    def clean_recommender_contact(self):
        recommender_contact = self.cleaned_data.get('recommender_contact')
        if not recommender_contact.isdigit():
            raise forms.ValidationError("Please enter a valid recommender contact number.")
        return recommender_contact