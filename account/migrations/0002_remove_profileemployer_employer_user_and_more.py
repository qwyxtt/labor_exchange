# Generated by Django 4.1.6 on 2023-04-04 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileemployer',
            name='employer_user',
        ),
        migrations.RemoveField(
            model_name='profileemployer',
            name='task',
        ),
        migrations.DeleteModel(
            name='ProfileEmployee',
        ),
        migrations.DeleteModel(
            name='ProfileEmployer',
        ),
    ]
