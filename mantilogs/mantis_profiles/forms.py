from django import forms
from django.core.exceptions import ValidationError

class Add_Culture_Log(forms.Form):
    culture_name = forms.CharField(help_text="Name of the culture to add log to.", required=True)
    # Todo: Form Validation Culture Name