# Generated by Django 4.1.6 on 2023-04-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0008_remove_task_descriptions_task_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
