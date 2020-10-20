# The forms for adding and modifying culture data.

from django.forms import ModelForm, HiddenInput
from .models import Log, Culture, Quarantine

class Create_Log_Form(ModelForm):
    class Meta:
        model = Log
        fields = ['culture', 'notes', 'added_feed', 'added_watering_media', 'cleaned_culture']
        widgets = {
            'culture': HiddenInput(),
        }

class Create_Culture_Form(ModelForm):
    class Meta:
        model = Culture
        fields = ['name', 'specie', 'feed', 'creation_date', 'parent_culture', 'retired', 'profile_picture', 'notes']


class Create_Quarantine_Form(ModelForm):
    class Meta:
        model = Quarantine
        fields = ['culture', 'start_date', 'end_date', 'reason']
