from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)

    token = models.CharField(max_length=200, verbose_name='токен', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания токена', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []