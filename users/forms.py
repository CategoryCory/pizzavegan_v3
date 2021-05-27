from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from allauth.account.forms import PasswordField, LoginForm, SignupForm


class CustomUserEditForm(UserEditForm):
    pass


class CustomUserCreationForm(UserCreationForm):
    pass


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'] = forms.EmailField(label='Email Address')
        self.fields['login'].widget.attrs['placeholder'] = 'Email'
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full rounded border-gray-400 focus:border-brand focus:ring-0 transition my-1'
            })


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label='Email Address')
        self.fields['password2'] = PasswordField(label='Confirm password')
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full rounded border-gray-400 focus:border-brand focus:ring-0 transition my-1'
            })
