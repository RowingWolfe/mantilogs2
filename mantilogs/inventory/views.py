from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.template.defaulttags import register
import datetime

from .models import Inventory, Item, Item_Consumption, Item_Expiration
from .forms import Add_Item_Form, Add_Order_Form, Add_Expiration_Date_Form, Item_Expired_Form, Add_Use_Form

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    items = get_list_or_404(Item)
    inventory = Inventory.objects.all()
    total_items = Item.objects.all().count()
    expirations = Item_Expiration.objects.all()
    a_week_from_today = datetime.date.today() + datetime.timedelta(days=7)
    context = {'user_info': request.user, 'page_title': 'Inventory Index',
                    'page_subtitle': f"Currently {total_items} Unique Item(s)", 'tab_info': 'Inventory Index',
                    'items': items, 'inventory': inventory, 'expirations': expirations,
               'a_week_from_today': a_week_from_today, 'today': datetime.date.today()
               }
    return render(request, 'inv_idx.html', context)


def add_item(request):
    """Add an item and add instance to inventory."""
    post_endpoint = f"/inventory/add_item/"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Add_Item_Form(request.POST, request.FILES)
            if form.is_valid():
                # Process the data.

                item = form.save()
                #Add an entry to Inventory.
                inv = Inventory(item=item)
                inv.save()
                # Redirect
                return HttpResponseRedirect('/inventory/index')
        else:
            return HttpResponseRedirect('/inventory/index')
    else:
        form = Add_Item_Form()


    return render(request, 'inv_add_item.html', {'tab_info': ' Add Item', 'form': form, 'user_info': request.user,
                                                 'endpoint': post_endpoint})

def add_order(request):
    """Add an item and add instance to inventory."""
    post_endpoint = f"/inventory/add_order/"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Add_Order_Form(request.POST, request.FILES)
            if form.is_valid():
                # Process the data.

                order = form.save()
                #Add an entry to Inventory.
                for item in form.cleaned_data['items']:
                    inv = Inventory.objects.get(item=item)
                    # I really need a way that the user can select how many of each item were bought.
                    inv.count += 1
                    inv.save()
                # Redirect
                return HttpResponseRedirect('/inventory/index')
        else:
            return HttpResponseRedirect('/inventory/index')
    else:
        form = Add_Order_Form()


    return render(request, 'inv_add_order.html', {'tab_info': ' Add Item', 'form': form, 'user_info': request.user,
                                                 'endpoint': post_endpoint})


def update_inventory(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            form = (request.POST, request.FILES)
            inv = Inventory.objects.get(item=request.POST['item'])
            inv.count = request.POST['count']
            inv.save()

        else:
            print("What the hell, someone trying to GET on this for?")
            return HttpResponseRedirect('/inventory/index')
    return HttpResponseRedirect('/inventory/index')


def add_expiration_date(request, item):
    """Add an item expiration date"""
    post_endpoint = f"/inventory/add_expiration_date/{item}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Add_Expiration_Date_Form(request.POST, request.FILES)
            if form.is_valid():
                # Process the data.

                form.save()
                # Redirect
                return HttpResponseRedirect('/inventory/index')
        else:
            return HttpResponseRedirect('/inventory/index')
    else:
        form = Add_Expiration_Date_Form()
        form.fields['item'].initial = item
    return render(request, 'inv_use_form.html', {'tab_info': ' Add Item', 'form': form, 'user_info': request.user,
                                                  'endpoint': post_endpoint})

def item_used(request, item):
    """Add an item expiration date"""
    post_endpoint = f"/inventory/item_used/{item}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Add_Use_Form(request.POST, request.FILES)
            if form.is_valid():
                # Process the data.

                used_item = form.save()
                inv = Inventory.objects.get(item=used_item.item)
                if inv.count >= 1:
                    inv.count -= 1
                    inv.save()
                # Redirect
                return HttpResponseRedirect('/inventory/index')
        else:
            return HttpResponseRedirect('/inventory/index')
    else:
        form = Add_Use_Form()
        form.fields['item'].initial = item
    return render(request, 'inv_use_form.html', {'tab_info': ' Add Item', 'form': form, 'user_info': request.user,
                                                  'endpoint': post_endpoint})

def item_expired(request, item):
    """Add an item expiration date"""
    post_endpoint = f"/inventory/item_expired/{item}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Item_Expired_Form(request.POST, request.FILES)
            if form.is_valid():
                # Process the data.

                used_item = form.save()
                inv = Inventory.objects.get(item=used_item.item)
                print(inv)
                if inv.count >= 1:
                    inv.count -= 1
                    inv.save()
                # Redirect
                return HttpResponseRedirect('/inventory/index')
        else:
            return HttpResponseRedirect('/inventory/index')
    else:
        form = Item_Expired_Form()
        form.fields['item'].initial = item
        form.fields['expired'].initial = True
    return render(request, 'inv_use_form.html', {'tab_info': ' Add Item', 'form': form, 'user_info': request.user,
                                                  'endpoint': post_endpoint})