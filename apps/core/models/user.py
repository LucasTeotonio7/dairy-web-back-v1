import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.core.models.mixins.user_manager import UserManager
from apps.core.models.mixins.timestamped_model import TimestampedModel


class User(TimestampedModel, AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True,)
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='profile/', max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        db_table = 'user'
        ordering = ['-is_active', '-last_login']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'
