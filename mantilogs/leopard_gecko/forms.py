from django.forms import ModelForm, HiddenInput
from .models import Log, Gecko, Tank_Cleaning_Log, Breeding_Log, Feeding_Log, Molt


class Create_Log_Form(ModelForm):
    class Meta:
        model = Log
        fields = ['gecko', 'defecation', 'behavior', 'problems', 'other_notes']
        widgets = {
            'gecko': HiddenInput(),
        }


class Create_Feed_Log_Form(ModelForm):
    class Meta:
        model = Feeding_Log
        fields = ['log', 'gecko', 'feed', 'feed_supplement', 'notes']
        widgets = {
            'gecko': HiddenInput(),
            'log': HiddenInput(),
        }


class Create_Molt_Form(ModelForm):
    class Meta:
        model = Molt
        fields = ['log', 'gecko', 'after_molt_picture', 'problems_with_molt', 'notes']
        widgets = {
            'gecko': HiddenInput(),
            'log': HiddenInput(),
        }


class Create_Gecko_Form(ModelForm):
    class Meta:
        model = Gecko
        fields = ['name', 'nickname', 'egg', 'birth_date', 'morphs', 'gender', 'personality', 'profile_picture', 'bio',
                  'caretaker_notes', 'caretaker']