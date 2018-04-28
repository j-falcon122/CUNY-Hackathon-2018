from django import forms
from .models import PotentialHost


class SearchForm(forms.Form):
    address = forms. CharField(
        max_length=200,
        label='Enter your address:',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id': 'pac-input',
                'placeholder': '55 Lexington Avenue, New York NY'
            }
        )
    )

#
# class HostForm(forms.Form):
#     name = forms.CharField(
#         max_length=45,
#         label = 'Organization name:',
#         widget=forms.TextInput()
#     )

class HostForm(forms.ModelForm):
    class Meta:
        model = PotentialHost
        fields = '__all__'
        # fields =['name']
        widgets = {
            forms.TextInput(attrs={
                'class': 'form-control',
            })
        }