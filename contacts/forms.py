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
            'message': forms.Textarea(attrs={'rows': 5})
        }
