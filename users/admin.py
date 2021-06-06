from django.contrib import admin
from .models import CustomUser
from profiles.models import PizzeriaLocation, MenuItem, Promotion


class PizzeriaLocationInline(admin.TabularInline):
    model = PizzeriaLocation
    extra = 0


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0


class PromotionInline(admin.TabularInline):
    model = Promotion
    extra = 0


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_active', ]
    list_editable = ['is_active', ]
    list_filter = ['is_active', ]
    list_per_page = 20
    fieldsets = (
        ('Account Information', {'fields': ('username', 'email', 'first_name', 'last_name', )}),
        ('Profile Information', {
            'fields': (
                'company_name', 'description', 'facebook', 'twitter', 'instagram', 'tiktok', 'youtube', 'online_ordering', 'pizzeria_logo', 
            )
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', )}),
        ('Important Dates', {'fields': ('last_login', 'date_joined', )}),
    )
    inlines = [
        PizzeriaLocationInline,
        MenuItemInline,
        PromotionInline
    ]


admin.site.register(CustomUser, CustomUserAdmin)
