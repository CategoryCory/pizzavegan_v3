from django.contrib import admin

from .models import PizzeriaSignupResponse, SurveyResponse, ContactUsResponse


class PizzeriaSignupResponseAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name', 'email_address', 'facebook_page', 'is_subscriber', 'is_approved', ]
    list_editable = ['is_approved', ]
    search_fields = ['restaurant_name', ]
    list_per_page = 25


class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ['email', 'pizza_description', ]


class ContactUsResponseAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', ]


admin.site.register(PizzeriaSignupResponse, PizzeriaSignupResponseAdmin)
admin.site.register(SurveyResponse, SurveyResponseAdmin)
admin.site.register(ContactUsResponse, ContactUsResponseAdmin)
