# Generated by Django 4.1.6 on 2023-02-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_remove_customuser_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(max_length=111, null=True),
        ),
    ]