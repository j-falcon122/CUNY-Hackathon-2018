from django import forms
from .models import Address

class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('address',)

    # your_address = forms.CharField(label='Your address', max_length=100)
