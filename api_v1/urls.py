from django.urls import path
from .views import pizzeria_list

app_name = 'api_v1'
urlpatterns = [
    path('pizzerias/', pizzeria_list, name='pizzeria_list'),
]
