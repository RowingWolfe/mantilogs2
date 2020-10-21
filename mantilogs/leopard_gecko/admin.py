from django.contrib import admin
from .models import Gecko, Log, Breeding_Log, Feeding_Log, Tank_Cleaning_Log, Molt, Clutch, Tank, Tank_Object, Death, Morph, Egg,Temperatures
# Register your models here.

admin.site.register(Gecko)
admin.site.register(Log)
admin.site.register(Egg)
admin.site.register(Feeding_Log)
admin.site.register(Tank_Cleaning_Log)
admin.site.register(Breeding_Log)
admin.site.register(Molt)
admin.site.register(Morph)
admin.site.register(Clutch)
admin.site.register(Tank)
admin.site.register(Tank_Object)
admin.site.register(Death)