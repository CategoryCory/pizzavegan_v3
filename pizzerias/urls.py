from django.urls import path

from .views import pizzeria_listings

app_name = 'pizzerias'
urlpatterns = [
    path('', pizzeria_listings, name='pizzeria_list'),
]
