from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
