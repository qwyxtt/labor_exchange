from django.db import models
from django.core.validators import MinValueValidator


class Employee(models.Model):
    user = models.OneToOneField('authentication.CustomUser', on_delete=models.CASCADE, null=True)
    skill = models.TextField(null=True)
    balance = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(limit_value=0.01)]
    )


class Employer(models.Model):
    user = models.OneToOneField('authentication.CustomUser', on_delete=models.CASCADE, null=True)
    balance = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(limit_value=0.01)]
    )


class Task(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    end_date = models.DateTimeField(null=True)
    cost = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(limit_value=0.01)]
    )
    owner = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)
    executor = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

# Task.objects.filter(owner__user=request.user)
