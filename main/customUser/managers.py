from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):

    def _create_user(self, phonenumber, password=None, **extra_fields):

        if not phonenumber:
            raise ValidationError('Номер телефона обязательный параметр')

        user = self.model(phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_user(self, phonenumber, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(phonenumber, password, **extra_fields)

    def create_superuser(self, phonenumber, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self._create_user(phonenumber, password, **extra_fields)
