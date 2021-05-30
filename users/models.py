from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=100, verbose_name='Company/Pizzeria Name')

    def __str__(self) -> str:
        return self.email
