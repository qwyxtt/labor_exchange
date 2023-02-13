from django.db import models
from authentication.models import CustomUser


class Account(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)

