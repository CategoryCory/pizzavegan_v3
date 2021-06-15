from typing import List
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from profiles.models import MenuItem, PizzeriaLocation

from .forms import ProfileUpdateForm, LocationUpdateForm, LocationFormSet, MenuItemForm

CustomUser = get_user_model()


class DashboardHomeView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'dashboard/dashboard-home.html'

    def get_object(self):
        return self.request.user


class UpdateProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'dashboard/dashboard-update-profile.html'
    success_url = reverse_lazy('dashboard:dashboard_home')
    success_message = 'Your profile has been successfully updated.'

    def get_object(self):
        return self.request.user


class PizzeriaLocationListView(LoginRequiredMixin, ListView):
    model = PizzeriaLocation
    template_name = 'dashboard/dashboard-store-locations.html'
    context_object_name = 'locations'

    def get_queryset(self):
        return PizzeriaLocation.objects.filter(profile=self.request.user)
    

@login_required
def pizzeria_location_create_view(request):
    customuser = request.user
    context = {}
    if request.method == 'POST':
        formset = LocationFormSet(request.POST, instance=customuser, queryset=PizzeriaLocation.objects.none())
        if formset.is_valid():
            formset.save()
            messages.add_message(request, messages.SUCCESS, 'Store locations successfully added.')
            return redirect(reverse_lazy('dashboard:dashboard_store_locations'))
        else:
            context['formset'] = formset
            return render(request, 'dashboard/dashboard-create-store-location.html', context)
    else:
        formset = LocationFormSet(instance=customuser, queryset=PizzeriaLocation.objects.none())
    context['formset'] = formset
    return render(request, 'dashboard/dashboard-create-store-location.html', context)


class PizzeriaLocationEditView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = PizzeriaLocation
    form_class = LocationUpdateForm
    template_name = 'dashboard/dashboard-update-store-location.html'
    success_url = reverse_lazy('dashboard:dashboard_store_locations')
    success_message = 'The store location has been successfully updated.'

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user


class PizzeriaLocationDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = PizzeriaLocation
    success_url = reverse_lazy('dashboard:dashboard_store_locations')
    success_message = 'Store location successfully deleted.'

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user


class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'dashboard/dashboard-menu-items.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return MenuItem.objects.filter(profile=self.request.user).order_by('-price')


class MenuItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'dashboard/dashboard-menu-item-form.html'
    success_url = reverse_lazy('dashboard:dashboard_menu_items')
    success_message = 'Menu item successfully added.'

    def get_context_data(self, **kwargs):
        context = super(MenuItemCreateView, self).get_context_data(**kwargs)
        context['page_action'] = 'Add'
        return context

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)


class MenuItemEditView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'dashboard/dashboard-menu-item-form.html'
    success_url = reverse_lazy('dashboard:dashboard_menu_items')
    success_message = 'Menu item successfully edited.'

    def get_context_data(self, **kwargs):
        context = super(MenuItemEditView, self).get_context_data(**kwargs)
        context['page_action'] = 'Edit'
        return context

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user


class MenuItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = MenuItem
    success_url = reverse_lazy('dashboard:dashboard_menu_items')
    success_message = 'Menu item successfully deleted.'

    def test_func(self):
        obj = self.get_object()
        return obj.profile == self.request.user


@login_required
def dashboard_promotions_view(request):
    return render(request, 'dashboard/dashboard-promotions.html')
