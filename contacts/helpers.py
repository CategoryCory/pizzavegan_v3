from django.conf import settings
import googlemaps


def geocode_address(street_addr, city, state):
    gmaps_key = settings.GEOCODING_API_KEY
    gmaps = googlemaps.Client(key=gmaps_key)
    result = gmaps.geocode(f'{street_addr}, {city}, {state}')
    lat_lng = {'lat': result[0]['geometry']['location']['lat'], 'lng': result[0]['geometry']['location']['lng']}
    return lat_lng
