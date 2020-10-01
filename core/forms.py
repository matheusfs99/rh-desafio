from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['logo', 'name', 'legal_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'legal_number': forms.TextInput(attrs={'class': 'form-control'})
        }