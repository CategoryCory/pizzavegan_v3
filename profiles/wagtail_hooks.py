from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import PizzeriaLocation


class PizzeriaLocationAdmin(ModelAdmin):
    model = PizzeriaLocation
    menu_label = 'Pizzeria Locations'
    menu_icon = 'list-ul'
    menu_order = 800
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = ['full_address', 'profile', ]
    list_filter = ['profile', ]
    search_fields = ['city', 'state', 'zip_code', ]
    list_per_page = 20


modeladmin_register(PizzeriaLocationAdmin)
