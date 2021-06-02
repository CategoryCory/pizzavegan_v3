from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from allauth.account.forms import ChangePasswordForm, PasswordField, LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm


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
    company_name = forms.CharField(max_length=100, label='Pizzeria Name')

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label='Email Address')
        self.fields['password2'] = PasswordField(label='Confirm password')
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['company_name'].widget.attrs['placeholder'] = 'Pizzeria Name'
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full rounded border-gray-400 focus:border-brand focus:ring-0 transition my-1'
            })
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.company_name = self.cleaned_data['company_name']
        user.save()
        return user


class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label='Email Address')
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs.update({
            'class': 'w-full rounded border-gray-400 focus:border-brand focus:ring-0 transition my-1'
        })


class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordKeyForm, self).__init__(*args, **kwargs)
        self.fields['password1'] = PasswordField(label='Enter new password')
        self.fields['password2'] = PasswordField(label='Confirm new password')
        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password2'].widget.attrs['placeholder'] = ''
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full rounded border-gray-400 focus:border-brand focus:ring-0 transition my-1'
            })
