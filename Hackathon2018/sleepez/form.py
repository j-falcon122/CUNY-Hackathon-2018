from django import forms


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