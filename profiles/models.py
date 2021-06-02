from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from contacts.helpers import geocode_address
import logging

CustomUser = get_user_model()
logger = logging.getLogger(__name__)


class PizzeriaProfile(models.Model):
    description = models.TextField(blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    online_ordering = models.URLField(max_length=200, blank=True)
    pizzeria_logo = models.ImageField(upload_to='images/pizzeria_logos/', blank=True)
    user_account = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user_account.company_name


class PizzeriaLocation(models.Model):
    street_address1 = models.CharField(max_length=100, blank=True, verbose_name='Street Address 1')
    street_address2 = models.CharField(max_length=100, blank=True, verbose_name='Street Address 2')
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=15, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    profile = models.ForeignKey(PizzeriaProfile, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.street_address1}, {self.city}, {self.state} {self.zip_code}'

    def save(self, *args, **kwargs):
        try:
            lat_lng = geocode_address(self.street_address1, self.city, self.state)
            self.latitude = lat_lng['lat']
            self.longitude = lat_lng['lng']
        except Exception as e:
            logger.error(f'Geocoding failed for {self}')
        super(PizzeriaLocation, self).save(*args, **kwargs)


class MenuItem(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    photo = models.ImageField(upload_to='images/menu_items/', blank=True)
    profile = models.ForeignKey(PizzeriaProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Promotion(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=False)
    begin_date = models.DateField(blank=False, default=date.today)
    end_date = models.DateField(blank=False, default=date.today)
    profile = models.ForeignKey(PizzeriaProfile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
