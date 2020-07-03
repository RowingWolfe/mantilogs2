from django.contrib import admin
from .models import Mantis, Logs, Picture, Environment_Log, Feeder_Culture, Feeder_Log, Gecko, Gecko_Log, Gecko_Morph
# Register your models here.

admin.site.register(Mantis)
admin.site.register(Logs)
admin.site.register(Picture)
admin.site.register(Environment_Log)
admin.site.register(Feeder_Culture)
admin.site.register(Feeder_Log)
admin.site.register(Gecko)
admin.site.register(Gecko_Log)
admin.site.register(Gecko_Morph)