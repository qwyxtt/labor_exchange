from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required


def signup(request):
    form = SignUpForm(request.POST or None)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = CustomUser.objects.create_user(
                firstname=cd['firstname'], lastname=cd['lastname'], email=cd['email'],
                is_active=True,
            )
            user.set_password(cd['password1'])
            user.save()

            return HttpResponse('success')
        error += 'User with such email already exists'

    return render(request, template_name='authentications/signup.html', context={
        'form': form,
        'title': 'Signup',
        'error': error
    })


def login_view(request):
    form = LoginForm(request.POST or None)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(firstname=cd['firstname'], password=cd['password'], email=cd['email'])
            if user is not None:
                login(request, user)
                return HttpResponse('success')
            error += 'Username or password are incorrect'
    return render(request, 'authentications/login.html', context={
        'form': form,
        'error': error
    })


@login_required
def logout_view(request):
    logout(request)
    return HttpResponse('success')
