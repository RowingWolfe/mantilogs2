from django.forms import ModelForm, HiddenInput
from .models import Item, Inventory, Item_Expiration, Item_Consumption,Order


class Add_Item_Form(ModelForm):
    class Meta:
        model = Item
        # Leaving out UPC for now, need to add the functionality.
        fields = ['name', 'brand', 'price', 'description', 'picture', 'item_type']
        # widgets = {
        #     'X': HiddenInput(),
        # }

class Add_Order_Form(ModelForm):
    class Meta:
        model = Order

        fields = ['items', 'order_id', 'total_cost', 'ordered_from', 'order_date']
        # widgets = {
        #     'X': HiddenInput(),
        # }

class Add_Use_Form(ModelForm):
    class Meta:
        model = Item_Consumption

        fields = ['item', 'date_consumed', 'expired', 'notes']
        widgets = {
            'item': HiddenInput(),
            'expired': HiddenInput(),
        }


class Item_Expired_Form(ModelForm):
    class Meta:
        model = Item_Consumption

        fields = ['item', 'date_consumed', 'expired', 'notes']
        widgets = {
            'item': HiddenInput(),
            'expired': HiddenInput(),
        }


class Add_Expiration_Date_Form(ModelForm):
    class Meta:
        model = Item_Expiration

        fields = ['item', 'expiration_date']
        widgets = {
            'item': HiddenInput(),
        }
