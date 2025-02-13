from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Inventory

# Form for user registration, extending the built-in UserCreationForm
class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField()  # Adding an email field to the form

    class Meta:
        model = User  # The form will create or update a User model
        fields = ['username', 'email', 'password1', 'password2']  # Fields to be included in the form

# Form for inventory items, extending the built-in ModelForm
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory  # The form will create or update an Inventory model
        fields = ['name', 'description', 'quantity', 'price']  # Fields to be included in the form