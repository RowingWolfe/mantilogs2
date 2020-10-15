from django import forms

from .models import Culture_Log
from django.core.exceptions import ValidationError

# class Add_Culture_Log(forms.Form):
#     culture_name = forms.CharField(help_text="Name of the culture to add log to.", required=True)
#     # Todo: Form Validation Culture Name

class Culture_Log_Form(forms.ModelForm):
    class Meta:
        model = Culture_Log
        fields = ['culture', 'log_notes', 'cleaned_culture_tank']