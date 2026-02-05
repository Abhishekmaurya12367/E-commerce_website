from django import forms
from .models import Accounts

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:  
        model = Accounts
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'password'huuu
        ]
