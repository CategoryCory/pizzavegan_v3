from django.forms.models import inlineformset_factory
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import CreateView

from profiles.models import PizzeriaLocation

from .forms import ProfileUpdateForm, LocationCreateForm, LocationUpdateForm, LocationFormSet

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
        current_user = self.request.user
        return PizzeriaLocation.objects.filter(profile=current_user)
    
    def get_context_data(self, **kwargs):
        context = super(PizzeriaLocationListView, self).get_context_data(**kwargs)
        context['customuser'] = self.request.user
        return context


class PizzeriaLocationCreateView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    model = PizzeriaLocation
    template_name = 'dashboard/dashboard-create-store-location.html'
    form_class = LocationCreateForm
    success_url = reverse_lazy('dashboard:dashboard-store-locations')
    success_message = 'New store location successfully added.'

    def get_context_data(self, **kwargs):
        context = super(PizzeriaLocationCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = LocationFormSet(self.request.POST, queryset=PizzeriaLocation.objects.none())
        else:
            context['formset'] = LocationFormSet(queryset=PizzeriaLocation.objects.none())
        context['customuser'] = self.request.user
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()


@login_required
def pizzeria_location_create_view(request):
    customuser = request.user
    # LocationFormSet = inlineformset_factory(CustomUser, PizzeriaLocation)
    context = { 'customuser': customuser }
    if request.method == 'POST':
        formset = LocationFormSet(request.POST, instance=customuser, queryset=PizzeriaLocation.objects.none())
        if formset.is_valid():
            formset.save()
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

    def get_context_data(self, **kwargs):
        context = super(PizzeriaLocationEditView, self).get_context_data(**kwargs)
        context['customuser'] = self.request.user
        return context

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


@login_required
def dashboard_menu_items_view(request):
    return render(request, 'dashboard/dashboard-menu-items.html')


@login_required
def dashboard_promotions_view(request):
    return render(request, 'dashboard/dashboard-promotions.html')
