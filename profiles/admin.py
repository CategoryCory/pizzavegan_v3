from django.contrib import admin
from .models import PizzeriaProfile, PizzeriaLocations, MenuItems, Promotions


class PizzeriaLocationsInline(admin.TabularInline):
    model = PizzeriaLocations
    extra = 0


class MenuItemsInline(admin.TabularInline):
    model = MenuItems
    extra = 0


class PromotionsInline(admin.TabularInline):
    model = Promotions
    extra = 0


class PizzeriaProfileAdmin(admin.ModelAdmin):
    list_display = ['user_account', ]
    list_per_page = 25
    inlines = [
        PizzeriaLocationsInline,
        MenuItemsInline,
        PromotionsInline
    ]


admin.site.register(PizzeriaProfile, PizzeriaProfileAdmin)
