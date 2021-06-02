from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_home_view(request):
    return render(request, 'dashboard/dashboard-home.html')


@login_required
def dashboard_store_locations_view(request):
    return render(request, 'dashboard/dashboard-store-locations.html')


@login_required
def dashboard_menu_items_view(request):
    return render(request, 'dashboard/dashboard-menu-items.html')


@login_required
def dashboard_promotions_view(request):
    return render(request, 'dashboard/dashboard-promotions.html')
