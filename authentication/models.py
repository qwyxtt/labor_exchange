from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .managers import MyUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    CHOICE_ACTIVITY = (
        ('employee', 'employee'),
        ('employer', 'employer')
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    location = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=False)
    activity = models.CharField(choices=CHOICE_ACTIVITY, null=True, max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyUserManager()
