from django.db import models
from authentication.models import CustomUser


class Task(models.Model):
    name = models.CharField(max_length=255)
    description_of_task = models.TimeField()


class employee(models.Model):
    user = models.OneToOneField(CustomUser)
    task = models.OneToOneField(Task)
