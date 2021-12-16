from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    USER_STATUS_LIST = (
        (0, 'client'),
        (1, 'manager'),
        (2, 'loader'),
        (3, 'driver'),
    )
    telefon = models.CharField('Телефон', max_length=12)
    role = models.IntegerField(choices=USER_STATUS_LIST, default=0)

    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'