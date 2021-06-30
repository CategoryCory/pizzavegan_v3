from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import PizzeriaLocation, MenuItem, Promotion

CustomUser = get_user_model()


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            'title',
            'description',
            'price',
            'photo',
        ]


class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promotion
        fields = [
            'title',
            'description',
            'begin_date',
            'end_date',
            'date_range',
        ]


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    menuitems = MenuItemSerializer(many=True, read_only=True)
    promotions = PromotionSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'company_name',
            'description',
            'facebook',
            'twitter',
            'instagram',
            'tiktok',
            'youtube',
            'online_ordering',
            'pizzeria_logo',
            'menuitems',
            'promotions',
        ]


class PizzeriaLocationSerializer(serializers.HyperlinkedModelSerializer):
    profile = CustomUserSerializer(read_only=True)

    class Meta:
        model = PizzeriaLocation
        fields = [
            'street_address1',
            'street_address2',
            'city',
            'state',
            'zip_code',
            'full_address',
            'phone',
            'dine_in',
            'carry_out',
            'delivery',
            'latitude',
            'longitude',
            'profile',
        ]