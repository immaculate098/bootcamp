from django import forms
from .models import Sitter, Student

class SitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = ['student', 'gender', 'on_duty']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'on_duty': forms.RadioSelect(choices=((True, 'On Duty'), (False, 'Off Duty'))),
        }

    def __init__(self, *args, **kwargs):
        super(SitterForm, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.all()
