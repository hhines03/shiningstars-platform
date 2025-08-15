from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('parent', 'Parent'),
    )
    role = models.CharField(max_length = 10, choices = ROLE_CHOICES, default = 'parent')
# Created two models one being the admin and the other being parent

class Child (models.Model):
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name = 'children')
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField()

# this function allows the system to assign the correct name to each object
    def __str__(self):
        return f"{self.first_name} {self.last_name}" 