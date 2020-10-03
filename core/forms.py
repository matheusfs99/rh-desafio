from django import forms
from .models import Company, Department

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['logo', 'name', 'legal_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'legal_number': forms.TextInput(attrs={'class': 'form-control'})
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }