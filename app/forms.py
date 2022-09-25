from django import forms

from . import models

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['name', 'email']

    # name = forms.CharField(label='Name', max_length=255)
    # email = forms.CharField(label='Email', max_length=255)
