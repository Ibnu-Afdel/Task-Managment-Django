from typing import Required
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    userid = models.CharField( max_length=50 , unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.userid
    