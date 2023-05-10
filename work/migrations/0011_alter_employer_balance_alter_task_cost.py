# Generated by Django 4.1.6 on 2023-05-10 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0010_alter_employer_balance_alter_task_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=0.01)]),
        ),
        migrations.AlterField(
            model_name='task',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(limit_value=0.01)]),
        ),
    ]