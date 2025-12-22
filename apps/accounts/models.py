from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        ordering = ('-created',)

    def __str__(self):
        return self.username
    
    @property
    def get_full_name(self):
        return self.full_name if self.full_name else self.username
