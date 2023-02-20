from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .managers import MyUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    CHOICE_ACTIVITY = (
        ('employee', 'employee'),
        ('employer', 'employer')
    )
    full_name = models.CharField(max_length=111, null=True)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    location = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=False)
    activity = models.CharField(choices=CHOICE_ACTIVITY, null=True, max_length=255)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyUserManager()
