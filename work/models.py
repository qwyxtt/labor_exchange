from django.db import models
from authentication.models import CustomUser


class Task(models.Model):
    name = models.CharField(max_length=255)
    description_of_task = models.TextField()


class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
