from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, UpdateView

# from profiles.models import PizzeriaProfile
from .forms import ProfileUpdateForm

CustomUser = get_user_model()


class DashboardHomeView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'dashboard/dashboard-home.html'

    def get_object(self):
        return self.request.user


class DashboardUpdateProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'dashboard/dashboard-update-profile.html'

    def get_object(self):
        return self.request.user

@login_required
def update_profile_view(request):
    return render(request, 'dashboard/dashboard-update-profile.html')


@login_required
def dashboard_store_locations_view(request):
    return render(request, 'dashboard/dashboard-store-locations.html')


@login_required
def dashboard_menu_items_view(request):
    return render(request, 'dashboard/dashboard-menu-items.html')


@login_required
def dashboard_promotions_view(request):
    return render(request, 'dashboard/dashboard-promotions.html')
