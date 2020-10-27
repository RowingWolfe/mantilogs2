from django.forms import ModelForm, HiddenInput
from .models import Log, Gecko, Tank_Cleaning_Log, Breeding_Log, Feeding_Log, Molt, Picture


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
        fields = [
            'name', 'nickname', 'egg', 'birth_date', 'morphs', 'gender', 'personality', 'profile_picture', 'bio',
            'caretaker_notes', 'caretaker', 'acquired_date', 'acquired_price', 'captive_bred', 'breeder_name',
            'breeder_email', 'weight', 'length'
        ]

class Create_Tank_Cleaning_Log(ModelForm):
    class Meta:
        model = Tank_Cleaning_Log
        fields = ['tank', 'date', 'full_tank_clean', 'cleaner_used', 'items_cleaned']
        widgets = {
            'tank': HiddenInput()
        }


class Add_Picture_Form(ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'gecko', 'picture', 'time', 'notes']
        widgets = {
            'gecko': HiddenInput()
        }