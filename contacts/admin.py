from django.contrib import admin

from .models import ContactUsResponse


class ContactUsResponseAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', ]


admin.site.register(ContactUsResponse, ContactUsResponseAdmin)
