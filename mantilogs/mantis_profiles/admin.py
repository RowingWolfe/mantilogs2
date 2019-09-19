from django.contrib import admin
from .models import Mantis, Logs, Picture, Environment_Log, Feeder_Culture, Feeder_Log
# Register your models here.

admin.site.register(Mantis)
admin.site.register(Logs)
admin.site.register(Picture)
admin.site.register(Environment_Log)
admin.site.register(Feeder_Culture)
admin.site.register(Feeder_Log)
