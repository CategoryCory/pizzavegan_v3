from typing import List
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, UpdateView

from profiles.models import PizzeriaLocation

from .forms import ProfileUpdateForm

CustomUser = get_user_model()


class DashboardHomeView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'dashboard/dashboard-home.html'

    def get_object(self):
        return self.request.user


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'dashboard/dashboard-update-profile.html'

    def get_object(self):
        return self.request.user


class PizzeriaLocationListView(LoginRequiredMixin, ListView):
    model = PizzeriaLocation
    template_name = 'dashboard/dashboard-store-locations.html'
    context_object_name = 'locations'

    def get_queryset(self):
        current_user = self.request.user
        return PizzeriaLocation.objects.filter(profile=current_user)
    
    def get_context_data(self, **kwargs):
        context = super(PizzeriaLocationListView, self).get_context_data(**kwargs)
        context['customuser'] = self.request.user
        return context


@login_required
def dashboard_store_locations_view(request):
    return render(request, 'dashboard/dashboard-store-locations.html')


@login_required
def dashboard_menu_items_view(request):
    return render(request, 'dashboard/dashboard-menu-items.html')


@login_required
def dashboard_promotions_view(request):
    return render(request, 'dashboard/dashboard-promotions.html')
