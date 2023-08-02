from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField('Заголовок поста', max_length=200)
    body = models.TextField('Текст поста')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"Пост {self.pk}"
