from django.db import models
from django.contrib.auth.models import AbstractUser

from listen.utils import BaseModel


class User(BaseModel, AbstractUser):
    """
    User
    """

    username = models.CharField(max_length=32, unique=True)
    avatar = models.URLField(max_length=500)
    bio = models.TextField()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
