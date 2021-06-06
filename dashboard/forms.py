from django import forms
from django.contrib.auth import get_user_model
from django.forms import widgets

CustomUser = get_user_model()

field_classes = 'w-full rounded border-gray-300 focus:border-brand focus:ring-0 transition mt-1 mb-4'


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
