from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .managers import MyUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    CHOICE_ACTIVITY = (
        ('employee', 'employee'),
        ('employer', 'employer')
    )
    firstname = models.CharField(max_length=111, null=True)
    lastname = models.CharField(max_length=111, null=True)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    location = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=False)
    activity = models.CharField(choices=CHOICE_ACTIVITY, null=True, max_length=255)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyUserManager()

    def full_name(self):
        return self.first_name + self.last_name

    def __str__(self):
        return f'{self.firstname} | {self.lastname}'
