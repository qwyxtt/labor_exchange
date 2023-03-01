from .models import CustomUser
from django import forms
from django.utils.timezone import now


class SignUpForm(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1950, int(now().year))))
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите почту'})
    )
    firstname = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите имя'})
    )
    lastname = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилия'})
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'})
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'firstname', 'lastname', 'password1', 'password2', 'activity')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
