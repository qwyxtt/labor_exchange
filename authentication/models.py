from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .managers import MyUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin) :
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()
