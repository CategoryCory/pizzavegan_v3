from django.urls import path

from .views import PizzeriaDetail, pizzeria_listings

app_name = 'pizzerias'
urlpatterns = [
    path('', pizzeria_listings, name='pizzeria_list'),
    path('<int:pk>/', PizzeriaDetail.as_view(), name='pizzeria_detail'),
]
