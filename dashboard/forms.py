from django import forms
from django.contrib.auth import get_user_model
from django.forms import widgets, inlineformset_factory

from profiles.models import PizzeriaLocation

CustomUser = get_user_model()

field_classes = 'w-full rounded border-gray-300 focus:border-brand focus:ring-0 transition mt-1 mb-4'
formset_classes = 'w-full border-0 border-b border-coolgray-300 focus:ring-0 focus:border-brand transition'


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


class LocationCreateForm(forms.ModelForm):
    class Meta:
        model = PizzeriaLocation
        fields = (
            'street_address1', 'street_address2', 'city', 'state', 'zip_code',
        )
        use_required_attribute = True


LocationFormSet = inlineformset_factory(
    CustomUser,
    PizzeriaLocation,
    form=LocationCreateForm,
    fields=(
        'street_address1', 'street_address2', 'city', 'state', 'zip_code',
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
    }
)


class LocationUpdateForm(forms.ModelForm):
    class Meta:
        model = PizzeriaLocation
        fields = (
            'street_address1', 'street_address2', 'city', 'state', 'zip_code',
        )
        widgets = {
            'street_address1': forms.TextInput(attrs={'class': field_classes}),
            'street_address2': forms.TextInput(attrs={'class': field_classes}),
            'city': forms.TextInput(attrs={'class': field_classes}),
            'state': forms.TextInput(attrs={'class': field_classes}),
            'zip_code': forms.TextInput(attrs={'class': field_classes}),
        }
