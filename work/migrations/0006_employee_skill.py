# Generated by Django 4.1.6 on 2023-02-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_employer_task_task_descriptions_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='skill',
            field=models.TextField(null=True),
        ),
    ]
