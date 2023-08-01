from django.db import models
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    title = models.CharField('Заголовок поста', max_length=200)
    body = models.TextField('Текст поста')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"Пост {self.pk}"


class User(AbstractUser):
    username = models.CharField('Имя пользователя', unique=True, max_length=150)
    email = models.EmailField('Email', blank=True, null=True)

    def __str__(self):
        return f"Пользователь {self.username}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'








# Create your models here.
