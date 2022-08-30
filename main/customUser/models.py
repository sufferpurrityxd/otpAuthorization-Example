from .validators import phonenumber_regex
from .managers import UserManager
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)


class User(AbstractBaseUser, PermissionsMixin):
    phonenumber = models.CharField(
        validators=[phonenumber_regex], max_length=12, verbose_name='Номер телефона', blank=False, null=False, unique=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )
    USERNAME_FIELD = 'phonenumber'

    objects = UserManager()

    def __str__(self):
        return self.phonenumber

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

