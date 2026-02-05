from django import forms
from .models import Accounts

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder':'Enter Password',
            'class':'form-control',
        })
    )
    confim_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder':'Enter confirm_Password'
        })
    )

    class Meta:  
        model = Accounts
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'password'
        ]

    def __init__(self, *args, **kwargs):
       super(RegistrationForm, self).__init__(*args, **kwargs)
       self.fields['first_name'].widget.attrs['class'] = 'Enter First Name'
       self.fields['last_name'].widget.attrs['class'] = 'Enter last Name'
       self.fields['email'].widget.attrs['class'] = 'Enter Email'
       self.fields['phone_number'].widget.attrs['class'] = 'Enter Phone_number'
       for field in self.fields:
        self.fields[field].widget.attrs['class'] = 'form-control'


