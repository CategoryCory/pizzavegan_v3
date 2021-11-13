from django.contrib import admin

from .models import PizzeriaLocation

class PizzeriaLocationAdmin(admin.ModelAdmin):
    list_display = ['full_address', 'profile', ]
    list_filter = ['profile', ]
    list_per_page = 20


admin.site.register(PizzeriaLocation, PizzeriaLocationAdmin)
