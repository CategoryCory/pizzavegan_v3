from django import forms
from django.utils.translation import gettext_lazy as _

from .models import ContactUsResponse, PizzeriaSignupResponse, SurveyResponse


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


class PizzeriaSignupResponseForm(forms.ModelForm):

    class Meta:
        model = PizzeriaSignupResponse
        fields = ('restaurant_name', 'email_address', 'vegan_pizza_type', 'menu_description', 'facebook_page',
                  'online_ordering_link', 'pizza_photo', 'is_subscriber')
        labels = {
            'restaurant_name': _('What is the name of your restaurant?'),
            'email_address': _('What is your email address?'),
            'vegan_pizza_type': _('Which vegan pizza would you like to feature in this promotion?'),
            'menu_description': _('Please provide a description of your pizza.'),
            'facebook_page': _('What is the link to your pizzeria\'s Facebook page?'),
            'online_ordering_link': _('What is your online ordering link?'),
            'pizza_photo': _('Please upload a photo of the pizza you would like to feature.'),
            'is_subscriber': _('Are you a PMQ subscriber?'),
        }
        help_texts = {
            'is_subscriber': _('Please check if you are a current subscriber to PMQ Pizza Magazine.'),
            'pizza_photo': _('Maximum file size: 5MB'),
        }


class SurveyResponseForm(forms.ModelForm):

    class Meta:
        model = SurveyResponse
        fields = ('email', 'pizza_description', )
        labels = {
            'email': _('If you\'d like to get updates from PizzaVegan.com, drop your email below:'),
            'pizza_description': _('Also, if there is a vegan pizza you\'d like to recommend or boast about, '
                                   'feel free to share it with us! Maybe it\'ll get featured in a future article on '
                                   'PizzaVegan.com!'),
        }
        widgets = {
            'pizza_description': forms.Textarea(attrs={'rows': 3})
        }
