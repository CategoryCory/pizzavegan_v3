from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=100, verbose_name='Company/Pizzeria Name')
    description = models.TextField(blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    tiktok = models.URLField(max_length=200, blank=True)
    youtube = models.URLField(max_length=200, blank=True)
    pizzeria_website = models.URLField(max_length=200, blank=True, verbose_name='Main Pizzeria Website')
    online_ordering = models.URLField(max_length=200, blank=True)
    pizzeria_logo = models.ImageField(upload_to='images/pizzeria_logos/', blank=True)

    def __str__(self) -> str:
        return self.email
    
    def get_absolute_url(self):
        return reverse("dashboard:dashboard_home", kwargs={})
    
