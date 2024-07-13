from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


ERROR_MESSAGES = {
    'unique': 'Пользователь с таким тегом уже существует',
    'max_length': 'Слишком длинный текст'
}


class User(AbstractUser):
    title = models.TextField(max_length=50, blank=True, verbose_name='О пользователе', error_messages={'max_length': ERROR_MESSAGES['max_length']})
    birthday = models.DateField(verbose_name='Дата рождения', null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name='Фото')
    country = models.CharField(max_length=60, blank=True, verbose_name='Страна', error_messages={'max_length': ERROR_MESSAGES['max_length']})
    city = models.CharField(max_length=85, blank=True, verbose_name='Город', error_messages={'max_length': ERROR_MESSAGES['max_length']})
    tag_user = models.CharField(max_length=20, verbose_name='Тег', unique=True, error_messages={'unique': ERROR_MESSAGES['unique']})
    telephone_number = models.CharField(max_length=18, verbose_name='Номер телефона')