from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.DashboardHomeView.as_view(), name='dashboard_home'),
    path('locations/', views.dashboard_store_locations_view, name='dashboard_store_locations'),
    path('menu-items/', views.dashboard_menu_items_view, name='dashboard_menu_items'),
    path('promotions/', views.dashboard_promotions_view, name='dashboard_promotions'),
]