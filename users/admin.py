from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_active', ]
    list_editable = ['is_active', ]
    list_filter = ['is_active', ]
    list_per_page = 20
    fieldsets = (
        ('Account Information', {'fields': ('username', 'email', 'first_name', 'last_name', 'company_name', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )}),
        ('Important Dates', {'fields': ('last_login', 'date_joined', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
