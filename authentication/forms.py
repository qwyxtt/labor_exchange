from .models import CustomUser
from django import forms
from django.utils.timezone import now


class SignUpForm(forms.ModelForm):
    CHOICE_ACTIVITY = (
        ('employee', 'employee'),
        ('employer', 'employer')
    )

    birthdate = forms.DateField(
        label='',
        widget=forms.SelectDateWidget(
            attrs={"class": "end-date-select"},
            years=range(1950, int(now().year))
        )
    )
    activity = forms.TypedChoiceField(choices=CHOICE_ACTIVITY, label='')
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
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
