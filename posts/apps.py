from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

    # class Meta:
    #     verbose_name = 'Пост'
    #     verbose_name_plural = 'Посты'
