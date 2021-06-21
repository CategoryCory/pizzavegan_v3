from profiles.helpers import geocode_zip
from profiles.models import PizzeriaLocation
from profiles.serializers import PizzeriaLocationSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view()
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def pizzeria_list(request):
    pizzeria_list = PizzeriaLocation.objects.all()
    source_zip = request.query_params.get('zip')
    radius = request.query_params.get('radius') if request.query_params.get('radius') is not None else 25
    return_dict: dict = {}
    if source_zip is not None:
        zip_latlng = geocode_zip(source_zip)

        if len(zip_latlng) == 0:
            return_dict['origin_status'] = 'NOT_FOUND'
            return Response(return_dict)
        else:
            lat_offset = float(radius) / 138
            lng_offset = float(radius) / 106
            pizzeria_list = pizzeria_list.filter(
                latitude__range=(zip_latlng['lat'] - lat_offset, zip_latlng['lat'] + lat_offset),
                longitude__range=(zip_latlng['lng'] - lng_offset, zip_latlng['lng'] + lng_offset)
            )
            return_dict['origin_status'] = 'OK'
            return_dict['origin_zip'] = source_zip
            return_dict['origin_latlng'] = [zip_latlng['lat'], zip_latlng['lng']]
    serializer = PizzeriaLocationSerializer(pizzeria_list, many=True, context={'request': request})
    return_dict['locations'] = serializer.data
    return Response(return_dict)
