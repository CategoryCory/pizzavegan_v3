from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ContactUsResponse


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUsResponse
        fields = ('name', 'email', 'message', )
        labels = {
            'name': _('Your name'),
            'email': _('Your email'),
            'message': _('What is your message?'),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full rounded border-gray-300 focus:border-brand focus:ring-0 '
                                                    'transition mt-1 mb-4'}),
            'email': forms.TextInput(attrs={'class': 'w-full rounded border-gray-300 focus:border-brand focus:ring-0 '
                                                     'transition mt-1 mb-4'}),
            'message': forms.Textarea(attrs={'rows': 5, 'class': 'w-full rounded border-gray-300 mt-1 '
                                                                 'focus:border-brand focus:ring-0 transition'}),
        }
