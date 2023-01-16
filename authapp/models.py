from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=254, blank=True, verbose_name='Email', unique=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Возраст')
    avatar = models.ImageField(upload_to='users', null=True, blank=True)