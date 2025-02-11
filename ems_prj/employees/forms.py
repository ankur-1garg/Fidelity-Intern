from django import forms
from .models import Employee

class EmployeeRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Employee
        fields = ['username', 'employee_id', 'email', 'date_of_joining', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data

class EmployeeLoginForm(forms.Form):
    employee_id = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())