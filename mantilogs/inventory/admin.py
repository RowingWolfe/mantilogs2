from django.contrib import admin
from .models import Item, Inventory, Item_Consumption, Order

# Register your models here.
admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(Item_Consumption)
admin.site.register(Order)