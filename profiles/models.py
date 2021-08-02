from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from .helpers import geocode_address
import datetime, logging

CustomUser = get_user_model()
logger = logging.getLogger(__name__)


class PizzeriaLocation(models.Model):
    street_address1 = models.CharField(max_length=100, blank=False, verbose_name='Street Address 1')
    street_address2 = models.CharField(max_length=100, blank=True, verbose_name='Street Address 2')
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=30, blank=False)
    zip_code = models.CharField(max_length=15, blank=False)
    phone = models.CharField(max_length=25, blank=True)
    location_website = models.URLField(max_length=200, blank=True)
    dine_in = models.BooleanField(default=False, verbose_name='Dine In')
    carry_out = models.BooleanField(default=False, verbose_name='Carry Out')
    delivery = models.BooleanField(default=False, verbose_name='Delivery')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='locations')

    @property
    def full_address(self):
        address_components = [self.street_address1]
        if self.street_address2 is not None and len(self.street_address2) > 0:
            address_components.append(self.street_address2)
        address_components.append(self.city)
        address_components.append(self.state)
        address_components.append(self.zip_code)
        return ', '.join(address_components)
            
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
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=False)
    photo = models.ImageField(upload_to='images/menu_items/', blank=True)
    profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='menuitems')

    def __str__(self) -> str:
        return self.title


class Promotion(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=False)
    begin_date = models.DateField(blank=False, default=date.today)
    end_date = models.DateField(blank=False, default=date.today)
    profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='promotions')

    def __str__(self) -> str:
        return self.title

    @property
    def date_range(self):
        dates = []
        if self.begin_date:
            dates.append(self.begin_date.strftime('%b %d, %Y'))
        if self.end_date:
            dates.append(self.end_date.strftime('%b %d, %Y'))
        return ' - '.join(dates)
