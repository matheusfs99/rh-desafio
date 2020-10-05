from django import forms
from .models import Company, Department, Employee

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


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'gender', 'phone', 'role', 'age', 'joining_date', 'salary', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'})
        }