from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from profiles.models import PizzeriaProfile


@login_required
def dashboard_home_view(request):
    profile = PizzeriaProfile.objects.get(user_account=request.user)

    context = {
        'user_name': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'company_name': request.user.company_name,
        'profile_description': profile.description,
        'profile_facebook': profile.facebook,
        'profile_twitter': profile.twitter,
        'profile_instagram': profile.instagram,
        'profile_tiktok': profile.tiktok,
        'profile_youtube': profile.youtube,
        'profile_online_ordering': profile.online_ordering,
        'profile_logo': profile.pizzeria_logo
    }
    return render(request, 'dashboard/dashboard-home.html', context)


@login_required
def dashboard_store_locations_view(request):
    return render(request, 'dashboard/dashboard-store-locations.html')


@login_required
def dashboard_menu_items_view(request):
    return render(request, 'dashboard/dashboard-menu-items.html')


@login_required
def dashboard_promotions_view(request):
    return render(request, 'dashboard/dashboard-promotions.html')
