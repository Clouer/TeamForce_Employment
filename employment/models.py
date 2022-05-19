from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    languages = models.CharField(max_length=200)
    hobbies = models.CharField(max_length=200)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Skill(models.Model):
    """Навыки"""
    name = models.CharField('Название', max_length=50)
    tag = models.CharField('Тег', max_length=15)
    users = models.ManyToManyField(User, verbose_name='пользователи', related_name='skills', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'skills'
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
