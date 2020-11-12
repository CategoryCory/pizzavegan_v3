from django.urls import path

from .views import PizzeriaList, PizzeriaDetail

app_name = 'pizzerias'
urlpatterns = [
    path('', PizzeriaList.as_view(), name='pizzeria_list'),
    path('<int:pk>/', PizzeriaDetail.as_view(), name='pizzeria_detail'),
]
