from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.DashboardHomeView.as_view(), name='dashboard_home'),
    path('edit/', views.UpdateProfileView.as_view(), name='dashboard_update_profile'),
    path('locations/', views.PizzeriaLocationListView.as_view(), name='dashboard_store_locations'),
    path('locations/add/', views.pizzeria_location_create_view, name='dashboard_create_store_location'),
    path('locations/edit/<int:pk>/', views.PizzeriaLocationEditView.as_view(), name='dashboard_edit_store_location'),
    path('locations/delete/<int:pk>/', views.PizzeriaLocationDeleteView.as_view(), name='dashboard_delete_store_location'),
    path('menu-items/', views.dashboard_menu_items_view, name='dashboard_menu_items'),
    path('promotions/', views.dashboard_promotions_view, name='dashboard_promotions'),
]