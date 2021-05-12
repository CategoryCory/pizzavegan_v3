from contacts.models import PizzeriaSignupResponse
from contacts.serializers import SignupResponseSerializer
from contacts.helpers import geocode_zip
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view()
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def signup_response_list(request):
    pizzeria_list = PizzeriaSignupResponse.objects.filter(is_approved=True)
    source_zip = request.query_params.get('zip')
    radius = request.query_params.get('radius')
    if source_zip is not None:
        if radius is not None:
            zip_latlng = geocode_zip(source_zip)
            lat_offset = float(radius) / 69.0
            lng_offset = float(radius) / 53.0
            pizzeria_list = pizzeria_list.filter(
                latitude__range=(zip_latlng['lat'] - lat_offset, zip_latlng['lat'] + lat_offset),
                longitude__range=(zip_latlng['lng'] - lng_offset, zip_latlng['lng'] + lng_offset)
            )
    serializer = SignupResponseSerializer(pizzeria_list, many=True)
    return Response(serializer.data)
