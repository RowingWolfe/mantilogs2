from django.contrib import admin
from .models import Mantis, Logs, Picture, Environment_Log, Culture, Culture_Log, Gecko, Gecko_Log, Gecko_Morph, \
    Mantis_Ooth, Gecko_Egg_Clutch, Inventory_Item, Inventory_Consumption, Purchase
# Register your models here.

class LogsAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    admin.site.register(Logs)

admin.site.register(Mantis)
admin.site.register(Picture)
admin.site.register(Environment_Log)
admin.site.register(Culture)
admin.site.register(Culture_Log)
admin.site.register(Gecko)
admin.site.register(Gecko_Log)
admin.site.register(Gecko_Morph)
admin.site.register(Mantis_Ooth)
admin.site.register(Gecko_Egg_Clutch)
admin.site.register(Inventory_Consumption)
admin.site.register(Inventory_Item)
admin.site.register(Purchase)