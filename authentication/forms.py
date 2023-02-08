from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'firstname', 'lastname', 'password1', 'password2')


class LoginForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
