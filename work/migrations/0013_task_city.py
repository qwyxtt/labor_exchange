# Generated by Django 4.2.1 on 2023-05-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0012_alter_employee_balance_alter_employer_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='city',
            field=models.CharField(choices=[('minsk', 'Минск'), ('grodno', 'Гродно'), ('brest', 'Брест'), ('vitebsk', 'Витебск'), ('mogilev', 'Могилев'), ('gomel', 'Гомель')], max_length=255, null=True),
        ),
    ]
