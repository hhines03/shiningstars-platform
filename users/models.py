from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('parent', 'Parent'),
    )
    role = models.CharField(max_length = 10, choices = ROLE_CHOICES, default = 'parent')
# Created two models one being the admin and the other being parent
