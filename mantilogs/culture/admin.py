from django.contrib import admin
from .models import Feed, Culture, Specie, Quarantine, Log
# Register your models here.

admin.site.register(Culture)
admin.site.register(Feed)
admin.site.register(Specie)
admin.site.register(Quarantine)
admin.site.register(Log)
