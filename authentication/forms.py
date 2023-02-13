from .models import CustomUser
from django import forms


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    birthdate = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = CustomUser
        fields = ('email', 'firstname', 'lastname', 'password1', 'password2', 'activity')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

