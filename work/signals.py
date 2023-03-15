from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from work.models import Employer, Employee

User = get_user_model()


@receiver(post_save, sender=User)
def create_activity(sender, instance, created, **kwargs):
    if created:
        if instance.activity == 'employee':
            Employee.objects.create(user=instance)
        else:
            Employer.objects.create(user=instance)



