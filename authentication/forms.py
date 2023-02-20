from .models import CustomUser
from django import forms
from django.utils.timezone import now


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1950, int(now().year))))

    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'password1', 'password2', 'activity')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

