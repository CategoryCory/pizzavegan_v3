from django import forms
from django.contrib.auth import get_user_model
from django.forms import widgets, inlineformset_factory

from profiles.models import PizzeriaLocation, MenuItem, Promotion

CustomUser = get_user_model()

field_classes = 'w-full rounded border-coolgray-300 focus:border-brand focus:ring-0 transition mt-1 mb-4'
formset_classes = 'w-full bg-transparent border-0 border-b border-coolgray-300 focus:ring-0 focus:border-brand transition'
checkbox_classes = 'rounded text-brand border-coolgray-600 focus:ring-brand'


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'company_name', 'description', 'facebook', 'twitter',
            'instagram', 'tiktok', 'youtube', 'online_ordering', 'pizzeria_logo',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': field_classes}),
            'last_name': forms.TextInput(attrs={'class': field_classes}),
            'company_name': forms.TextInput(attrs={'class': field_classes}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': field_classes}),
            'facebook': forms.URLInput(
                attrs={'class': field_classes, 'placeholder': 'https://facebook.com/your-company-page'}
            ),
            'twitter': forms.URLInput(
                attrs={'class': field_classes, 'placeholder': 'https://twitter.com/your-company-page'}
            ),
            'instagram': forms.URLInput(
                attrs={'class': field_classes, 'placeholder': 'https://instagram.com/your-company-page'}
            ),
            'tiktok': forms.URLInput(
                attrs={'class': field_classes, 'placeholder': 'https://tiktok.com/your-company-page'}
            ),
            'youtube': forms.URLInput(
                attrs={'class': field_classes, 'placeholder': 'https://youtube.com/your-company-page'}
            ),
            'online_ordering': forms.URLInput(
                attrs={'class': field_classes, 'placeholder': 'https://sample-online-ordering.com'}
            ),
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model = PizzeriaLocation
        fields = (
            'street_address1', 'street_address2', 'city', 'state', 'zip_code', 'phone', 'dine_in', 'carry_out', 'delivery',
        )
        widgets = {
            'street_address1': forms.TextInput(attrs={'class': field_classes}),
            'street_address2': forms.TextInput(attrs={'class': field_classes}),
            'city': forms.TextInput(attrs={'class': field_classes}),
            'state': forms.TextInput(attrs={'class': field_classes}),
            'zip_code': forms.TextInput(attrs={'class': field_classes}),
            'phone': forms.TextInput(attrs={'class': field_classes}),
            'dine_in': forms.CheckboxInput(attrs={'class': checkbox_classes}),
            'carry_out': forms.CheckboxInput(attrs={'class': checkbox_classes}),
            'delivery': forms.CheckboxInput(attrs={'class': checkbox_classes}),
        }


LocationFormSet = inlineformset_factory(
    CustomUser,
    PizzeriaLocation,
    form=LocationForm,
    fields=(
        'street_address1', 'street_address2', 'city', 'state', 'zip_code', 'phone', 'dine_in', 'carry_out', 'delivery',
    ),
    extra=1,
    max_num=10,
    absolute_max=10,
    widgets={
        'street_address1': widgets.TextInput(attrs={'class': formset_classes, 'placeholder': ' ', 'required': 'true'}),
        'street_address2': widgets.TextInput(attrs={'class': formset_classes, 'placeholder': ' '}),
        'city': widgets.TextInput(attrs={'class': formset_classes, 'placeholder': ' ', 'required': 'true'}),
        'state': widgets.TextInput(attrs={'class': formset_classes, 'placeholder': ' ', 'required': 'true'}),
        'zip_code': widgets.TextInput(attrs={'class': formset_classes, 'placeholder': ' ', 'required': 'true'}),
        'phone': widgets.TextInput(attrs={'class': formset_classes, 'placeholder': ' '}),
        'dine_in': widgets.CheckboxInput(attrs={'class': checkbox_classes}),
        'carry_out': widgets.CheckboxInput(attrs={'class': checkbox_classes}),
        'delivery': widgets.CheckboxInput(attrs={'class': checkbox_classes}),
    }
)


class MenuItemForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields = (
            'title', 'description', 'price', 'photo', 
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': field_classes}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': field_classes}),
            'price': forms.NumberInput(attrs={'class': field_classes, 'min': 0, 'max': 999.99}),
        }
        labels = {
            'price': 'Price (omit dollar sign)'
        }


class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = (
            'title', 'begin_date', 'end_date', 'description',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': field_classes}),
            'begin_date': forms.DateInput(attrs={'class': field_classes, 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': field_classes, 'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': field_classes}),
        }
