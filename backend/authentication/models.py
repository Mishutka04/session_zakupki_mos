from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name="Никнейм", unique=True)
    password = models.CharField(max_length=50, verbose_name="Пароль")
    # Override groups field with a unique related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Ensure this is unique
        blank=True,
        help_text='The groups this user belongs to.'
    )

    # Override user_permissions field with a unique related_name
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Ensure this is unique
        blank=True,
        help_text='Specific permissions for this user.'
    )
# Create your models here.