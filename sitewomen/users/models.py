from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True, null=True, verbose_name='Фото')
    date_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    class Meta:
        db_table = 'auth_user'
