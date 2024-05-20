from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name': 'Name',
            'gender': 'Gender',
            'location': 'Location',
            'date_of_birth': 'Date of Birth',
            'nin': 'NIN',
            'religion': 'Religion',
            'education': 'Education',
            'contact': 'Contact',
            'sitter_number': 'Sitter Number',
            'next_of_kin': 'Next of Kin',
            'recommender_name': 'Recommender Name',
            'recommender_contact': 'Recommender Contact',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}), 
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'nin': forms.NumberInput(attrs={'class': 'form-control'}),
            'religion': forms.TextInput(attrs={'class': 'form-control'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'sitter_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'next_of_kin': forms.TextInput(attrs={'class': 'form-control'}),
            'recommender_name': forms.TextInput(attrs={'class': 'form-control'}),
            'recommender_contact': forms.NumberInput(attrs={'class': 'form-control'}),
        }

