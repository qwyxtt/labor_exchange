# Generated by Django 4.1.6 on 2023-05-22 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0013_task_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='city',
        ),
    ]