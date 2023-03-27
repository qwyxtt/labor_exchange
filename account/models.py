from django.db import models


class ProfileEmployer(models.Model):
    employer_user = models.OneToOneField('work.Employer', on_delete=models.CASCADE, null=True)
    task = models.ForeignKey('work.Task', on_delete=models.CASCADE, null=True)


class ProfileEmployee(models.Model):
    employee_user = models.OneToOneField('work.Employee', on_delete=models.CASCADE, null=True)
