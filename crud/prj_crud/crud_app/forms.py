from django import forms
from crud_app.models import Orders


class contactForm(forms.ModelForm):
    name = forms .CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=False)
    message = forms.CharField(max_length=100, required=True)


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['order_id', 'name', 'price', 'email', 'addr']
