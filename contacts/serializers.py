from .models import PizzeriaSignupResponse
from rest_framework import serializers


class SignupResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PizzeriaSignupResponse
        fields = [
            'id',
            'restaurant_name',
            'email_address',
            'street_address1',
            'street_address2',
            'city',
            'state',
            'zip_code',
            'latitude',
            'longitude',
            'vegan_pizza_type',
            'menu_description',
        ]
