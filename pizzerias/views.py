from django.views.generic import ListView, DetailView
from django.conf import settings

from contacts.models import PizzeriaSignupResponse


class PizzeriaList(ListView):

    model = PizzeriaSignupResponse
    template_name = 'pizzerias/pizzeria_list.html'
    queryset = PizzeriaSignupResponse.objects.filter(is_approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maps_api_key'] = settings.MAPS_API_KEY
        return context


class PizzeriaDetail(DetailView):

    model = PizzeriaSignupResponse
    template_name = 'pizzerias/pizzeria_detail.html'
    context_object_name = 'pizzeria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maps_api_key'] = settings.MAPS_API_KEY
        return context
