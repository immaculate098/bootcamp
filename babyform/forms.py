from django import forms
from .models import Baby, Sitter

class BabyForm(forms.ModelForm):
    assigned_sitter = forms.ModelChoiceField(queryset=None, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_sitter'].queryset = Sitter.objects.filter(is_on_duty=True)

    class Meta:
        model = Baby
        fields = '__all__'
        widgets = {
            'fee': forms.TextInput(attrs={'type': 'text'}),
        }
