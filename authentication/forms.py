from django.contrib.auth.forms import (UserCreationForm,
                                          UsernameField)
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _

class RegistrationForm(UserCreationForm):
    email = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': "form-control",
             'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': "form-control",
             'placeholder': 'Repeat Password'})


class CustomAuthenticationForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class': 'form-control'}),
    )
