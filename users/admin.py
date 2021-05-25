from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Account Information', {'fields': ('username', 'email', 'first_name', 'last_name', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )}),
        ('Important Dates', {'fields': ('last_login', 'date_joined', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
