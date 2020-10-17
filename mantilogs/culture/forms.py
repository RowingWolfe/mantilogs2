# The forms for adding and modifying culture data.

from django.forms import ModelForm
from .models import Log

class Create_Log_Form(ModelForm):
    class Meta:
        model = Log
        fields = ['culture', 'notes', 'added_feed', 'added_watering_media', 'cleaned_culture']

