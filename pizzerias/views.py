from django.views.generic import DetailView
from django.shortcuts import render
from django.conf import settings
from geopy import distance

from contacts.helpers import geocode_zip
from contacts.models import PizzeriaSignupResponse


def pizzeria_listings(request):
    pizzeria_list = PizzeriaSignupResponse.objects.filter(is_approved=True)
    maps_api_key = settings.MAPS_API_KEY
    search_zip = request.GET.get('zip')
    map_center = {'lat': 39.8283, 'lng': -98.5795}
    closest_pizzeria_dist = None
    error = None

    if search_zip:
        try:
            zip_latlng = geocode_zip(search_zip)
            source_location = (zip_latlng['lat'], zip_latlng['lng'])
            for pizzeria in pizzeria_list:
                dest_location = (pizzeria.latitude, pizzeria.longitude)
                pizz_distance = round(distance.distance(source_location, dest_location).miles, 1)
                pizzeria.__dict__['dist_from_source'] = pizz_distance
            pizzeria_list = sorted(pizzeria_list, key=lambda p: p.dist_from_source)
            map_center = zip_latlng
            closest_pizzeria_dist = pizzeria_list[0].dist_from_source
        except IndexError:
            error = "There was a problem finding that ZIP code. Please try another value."

    context = {
        'maps_api_key': maps_api_key,
        'pizzeria_list': pizzeria_list,
        'search_zip': search_zip,
        'map_center': map_center,
        'error': error,
        'closest_pizzeria_dist': closest_pizzeria_dist,
    }

    return render(request, 'pizzerias/pizzeria_list.html', context)


class PizzeriaDetail(DetailView):
    model = PizzeriaSignupResponse
    template_name = 'pizzerias/pizzeria_detail.html'
    context_object_name = 'pizzeria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maps_api_key'] = settings.MAPS_API_KEY
        return context
