from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom User Model"""
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    about_text = models.TextField(blank=True, max_length=50,  verbose_name='About', null=True, default='Hi There')
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
