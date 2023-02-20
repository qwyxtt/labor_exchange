from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def _create_user(self, email, full_name, password1, birthdate, activity,  **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        if not full_name:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            birthdate=birthdate,
            activity=activity,
            **extra_fields,
        )
        user.set_password(password1)
        user.save(using=self._db)
        return user

    def create_user(self, email, full_name, password1, birthdate, activity):
        return self._create_user(email, full_name, password1, birthdate, activity)

    def create_superuser(self, email, full_name, password1, birthdate, activity):
        return self._create_user(email, full_name, password1, birthdate, activity, is_staff=True,
                                 is_superuser=True)
