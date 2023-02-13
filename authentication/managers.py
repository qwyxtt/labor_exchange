from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password1, **extra_fields):
        if not email:


            raise ValueError("Вы не ввели Email")
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password1)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password1):
        return self._create_user(email, username, password1)

    def create_superuser(self, email, username, password1):
        return self._create_user(email, username, password1, is_staff=True, is_superuser=True)
