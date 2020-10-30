from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.template.defaulttags import register
from .models import Gecko, Log, Breeding_Log, Feeding_Log, Tank_Cleaning_Log, Molt, Morph_Combo, Clutch, Tank, Tank_Object, Death, Morph, Egg,Temperatures, Picture
from .forms import Create_Log_Form, Create_Feed_Log_Form, Create_Molt_Form, Create_Gecko_Form, Create_Tank_Cleaning_Log, Add_Picture_Form, Add_Measurement_Form

import datetime

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    """Display a full list of all active cultures with links to their profiles, add log, add quarantine."""
    geckos = get_list_or_404(Gecko)
    last_logs = {}
    full_tank_clean_logs = {}
    last_10_cleaning_logs = {}
    last_water_bowl_cleaning_logs = {}
    last_food_bowl_cleaning_logs = {}
    last_fed = {}
    last_vitd = {}
    last_multivit = {}
    last_defecation = {}
    last_molt = {}
    total_geckos = 0
    today = datetime.datetime.now()
    a_week = datetime.timedelta(days=7)
    a_month = datetime.timedelta(days=30)
    four_days = datetime.timedelta(days=4)
    for gecko in geckos:
        total_geckos += 1
        # Find logs for Gecko
        if (Log.objects.filter(gecko=gecko)):
            last_logs[gecko] = Log.objects.filter(
                gecko=gecko).latest('time')

        # Get last tank cleaning information.
        try:
            if Tank.objects.get(gecko=gecko):
                tank = Tank.objects.get(gecko=gecko)

                if Tank_Cleaning_Log.objects.filter(tank=tank, full_tank_clean=True):
                    full_tank_clean_logs[gecko.id] = Tank_Cleaning_Log.objects.filter(tank=tank, full_tank_clean=True).latest('date').date
                    last_10_cleaning_logs[gecko.id] = Tank_Cleaning_Log.objects.filter(tank=tank).order_by('date')[:10]

                if Tank_Cleaning_Log.objects.filter(tank=tank, items_cleaned__icontains="Water Bowl"):
                    last_water_bowl_cleaning_logs[gecko.id] = Tank_Cleaning_Log.objects.filter(tank=tank,
                                                            items_cleaned__icontains="Water Bowl").latest('date').date

                if Tank_Cleaning_Log.objects.filter(tank=tank, items_cleaned__icontains="Food Bowl"):
                    last_food_bowl_cleaning_logs[gecko.id] = Tank_Cleaning_Log.objects.filter(tank=tank,
                                                            items_cleaned__icontains="Food Bowl").latest('date').date
                    #print(type(Tank_Cleaning_Log.objects.filter(tank=tank,
                    #                                        items_cleaned__icontains="Food Bowl").latest('date').date))

        except Tank.DoesNotExist:
            pass

        try:
            if Feeding_Log.objects.filter(gecko=gecko):
                last_fed[gecko.id] = Feeding_Log.objects.filter(gecko=gecko).latest('time').time

                if Feeding_Log.objects.filter(gecko=gecko, feed_supplement="VITD"):
                    last_vitd[gecko.id] = Feeding_Log.objects.filter(gecko=gecko, feed_supplement="VITD").latest('time').time

                if Feeding_Log.objects.filter(gecko=gecko, feed_supplement="MULT"):
                    last_multivit[gecko.id] = Feeding_Log.objects.filter(gecko=gecko, feed_supplement="MULT").latest('time').time
        except Feeding_Log.DoesNotExist:
            pass

        try:
            if Log.objects.filter(gecko=gecko, defecation=True):
                last_defecation[gecko.id] = Log.objects.filter(gecko=gecko, defecation=True).latest('time').time
        except Log.DoesNotExist:
            pass

        try:
            if Molt.objects.filter(gecko=gecko):
                last_molt[gecko.id] = Molt.objects.filter(gecko=gecko).latest('time').time
        except Molt.DoesNotExist:
            pass

    return render(request, 'leo_idx.html', {'geckos': geckos, 'last_logs': last_logs,'full_tank_cleans': full_tank_clean_logs,
                                            'last_10_cleans': last_10_cleaning_logs, 'last_water_bowl_cleans': last_water_bowl_cleaning_logs,
                                            'last_food_bowl_cleans': last_food_bowl_cleaning_logs, 'last_vitd': last_vitd,
                                            'last_multivit': last_multivit, 'last_fed': last_fed, 'last_defecation': last_defecation,
                                            'last_molt': last_molt,
                                                'user_info': request.user, 'page_title': 'Leopard Gecko Index',
                                                'page_subtitle': f"Currently {total_geckos} Geckos", 'tab_info': 'Leopard Gecko Index',
                                            'today': today, 'a_week_ago': today - a_week, 'four_days_ago': today - four_days,
                                            'a_month_ago': today - a_month})


def profile(request, gecko):
    """Gather all required info for the Gecko itself. Tabbed info will be in sub-views and ajaxed in."""
    gecko = get_object_or_404(Gecko, id=gecko)
    morphs = gecko.morphs.all()
    context = {'user_info': request.user, 'gecko': gecko, 'morphs': morphs, 'tab_info': gecko.name}
    return render(request, 'leo_prof.html', context)



def info_partial(request, gecko):
    gecko = get_object_or_404(Gecko, id=gecko)
    last_logs = {}
    full_tank_clean_logs = {}
    last_10_cleaning_logs = {}
    last_water_bowl_cleaning_logs = {}
    last_food_bowl_cleaning_logs = {}
    last_fed = {}
    last_vitd = {}
    last_multivit = {}
    last_defecation = {}
    last_molt = {}
    # Find logs for Gecko
    if (Log.objects.filter(gecko=gecko)):
        last_logs[gecko] = Log.objects.filter(
            gecko=gecko).latest('time')

    # Get last tank cleaning information.
    try:
        if Tank.objects.get(gecko=gecko):
            tank = Tank.objects.get(gecko=gecko)

            if Tank_Cleaning_Log.objects.filter(tank=tank, full_tank_clean=True):
                full_tank_clean_logs[gecko.id] = Tank_Cleaning_Log.objects.filter(tank=tank,
                                                                                  full_tank_clean=True).latest(
                    'date').date
                last_10_cleaning_logs[gecko.id] = Tank_Cleaning_Log.objects.filter(tank=tank).order_by('date')[:10]

            if Tank_Cleaning_Log.objects.filter(tank=tank, items_cleaned__icontains="Water Bowl"):
                last_water_bowl_cleaning_logs[gecko.id] = Tank_Cleaning_Log.objects.filter(tank=tank,
                                                                                           items_cleaned__icontains="Water Bowl").latest(
                    'date').date

            if Tank_Cleaning_Log.objects.filter(tank=tank, items_cleaned__icontains="Food Bowl"):
                last_food_bowl_cleaning_logs[gecko.id] = Tank_Cleaning_Log.objects.filter(tank=tank,
                                                                                          items_cleaned__icontains="Food Bowl").latest(
                    'date').date

    except Tank.DoesNotExist:
        pass

    try:
        if Feeding_Log.objects.filter(gecko=gecko):
            last_fed[gecko.id] = Feeding_Log.objects.filter(gecko=gecko).latest('time').time

            if Feeding_Log.objects.filter(gecko=gecko, feed_supplement="VITD"):
                last_vitd[gecko.id] = Feeding_Log.objects.filter(gecko=gecko, feed_supplement="VITD").latest(
                    'time').time

            if Feeding_Log.objects.filter(gecko=gecko, feed_supplement="MULT"):
                last_multivit[gecko.id] = Feeding_Log.objects.filter(gecko=gecko, feed_supplement="MULT").latest(
                    'time').time
    except Feeding_Log.DoesNotExist:
        pass

    try:
        if Log.objects.filter(gecko=gecko, defecation=True):
            last_defecation[gecko.id] = Log.objects.filter(gecko=gecko, defecation=True).latest('time').time
    except Log.DoesNotExist:
        pass

    try:
        if Molt.objects.filter(gecko=gecko):
            last_molt[gecko.id] = Molt.objects.filter(gecko=gecko).latest('time').time
    except Molt.DoesNotExist:
        pass
    context = {'last_logs': last_logs,'full_tank_cleans': full_tank_clean_logs,
                'last_10_cleans': last_10_cleaning_logs, 'last_water_bowl_cleans': last_water_bowl_cleaning_logs,
                'last_food_bowl_cleans': last_food_bowl_cleaning_logs, 'last_vitd': last_vitd,
                'last_multivit': last_multivit, 'last_fed': last_fed, 'last_defecation': last_defecation,
                 'last_molt': last_molt, 'gecko': gecko
               }
    return render(request, 'leo_info_partial.html', context)


def log_partial(request, log):
    """Gets individual log for logs_partial"""
    log = get_object_or_404(Log, id=log)
    feed_log = {}
    molt_log = {}
    try:
        feed_log = Feeding_Log.objects.filter(log=log).latest('time')
    except Feeding_Log.DoesNotExist:
        pass
    try:
        molt_log = Molt.objects.filter(log=log).latest('time')
    except Molt.DoesNotExist:
        pass
    #print(log, feed_log, molt_log)

    context = {'user_info': request.user, 'log': log, 'feed_log': feed_log, 'molt_log': molt_log}
    return render(request, 'leo_log_partial.html', context)


def logs_partial(request, gecko):
    """Gets logs for gecko, loads the logs partial."""
    gecko = get_object_or_404(Gecko, id=gecko)
    logs = Log.objects.filter(gecko=gecko).order_by('-time')
    log_count = logs.count()

    context = {'user_info': request.user, 'gecko': gecko, 'logs': logs, 'log_count': log_count}
    return render(request, 'leo_logs_partial.html', context)


def add_log(request, gecko):
    """Add a Log to a gecko. Renders a form and takes the post request for it."""
    gecko = get_object_or_404(Gecko, id=gecko)
    post_endpoint = f"/leopard_gecko/add_log/{gecko.id}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Log_Form(request.POST)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/profile/'+str(gecko.id))
        else:
            return HttpResponseRedirect('/leopard_gecko/profile/'+ str(gecko.id))
    else:
        form = Create_Log_Form()
        form.fields['gecko'].initial = gecko

    return render(request, 'leo_log_form.html', {'tab_info': gecko.name + ' Add log',
                                                 'form': form, 'gecko': gecko, 'user_info': request.user, 'endpoint': post_endpoint})


def edit_log(request, gecko, log):
    """Edit a Log to a gecko. Renders a form and takes the post request for it."""
    gecko = get_object_or_404(Gecko, id=gecko)
    log = get_object_or_404(Log, id=log)
    post_endpoint = f"/leopard_gecko/edit_log/{gecko.id}/{log.id}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Log_Form(request.POST, instance=log)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/profile/'+str(gecko.id))
        else:
            return HttpResponseRedirect('/leopard_gecko/profile/'+ str(gecko.id))
    else:
        form = Create_Log_Form(instance=log)
        form.fields['gecko'].initial = gecko

    return render(request, 'leo_log_form.html', {'tab_info': gecko.name + ' edit log', 'form': form, 'gecko': gecko, 'user_info': request.user, 'endpoint': post_endpoint})


def add_feed_log(request, gecko, log):
    """Add a Log to a gecko. Renders a form and takes the post request for it."""
    gecko = get_object_or_404(Gecko, id=gecko)
    log = get_object_or_404(Log, id=log)
    post_endpoint = f"/leopard_gecko/add_feed_log/{gecko.id}/{log.id}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Feed_Log_Form(request.POST)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/profile/'+str(gecko.id))
        else:
            return HttpResponseRedirect('/leopard_gecko/profile/'+ str(gecko.id))
    else:
        form = Create_Feed_Log_Form()
        form.fields['gecko'].initial = gecko
        #print(form.fields)
        form.fields['log'].initial = log

    return render(request, 'leo_log_form.html', {'tab_info': gecko.name + ' Feed log', 'form': form, 'gecko': gecko, 'user_info': request.user, 'endpoint': post_endpoint})


def edit_feed_log(request, gecko, log):
    """Add a Log to a gecko. Renders a form and takes the post request for it."""
    gecko = get_object_or_404(Gecko, id=gecko)
    feed_log = get_object_or_404(Feeding_Log, id=log)
    post_endpoint = f"/leopard_gecko/edit_feed_log/{gecko.id}/{feed_log.id}" #The feed_log's log id.
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Feed_Log_Form(request.POST, instance=feed_log)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/profile/'+str(gecko.id))
        else:
            return HttpResponseRedirect('/leopard_gecko/profile/'+ str(gecko.id))
    else:
        form = Create_Feed_Log_Form(instance=feed_log)
        print(form.fields)
        form.fields['gecko'].initial = gecko
        form.fields['log'].initial = feed_log.log

    return render(request, 'leo_log_form.html', {'tab_info': gecko.name + ' Feed log','form': form, 'gecko': gecko, 'user_info': request.user, 'endpoint': post_endpoint})


def add_molt(request, gecko, log):
    """Add a Log to a gecko. Renders a form and takes the post request for it."""
    gecko = get_object_or_404(Gecko, id=gecko)
    log = get_object_or_404(Log, id=log)
    post_endpoint = f"/leopard_gecko/add_molt/{gecko.id}/{log.id}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Molt_Form(request.POST, request.FILES)
            print('FILES SENT:',request.FILES)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/profile/'+str(gecko.id))
        else:
            return HttpResponseRedirect('/leopard_gecko/profile/'+ str(gecko.id))
    else:
        form = Create_Molt_Form()
        form.fields['gecko'].initial = gecko
        #print(form.fields)
        form.fields['log'].initial = log

    return render(request, 'leo_log_form.html', {'tab_info': gecko.name + ' Molt log', 'form': form, 'gecko': gecko, 'user_info': request.user, 'endpoint': post_endpoint})


def edit_molt(request, gecko, log):
    """Add a Log to a gecko. Renders a form and takes the post request for it."""
    gecko = get_object_or_404(Gecko, id=gecko)
    molt = get_object_or_404(Molt, id=log)
    post_endpoint = f"/leopard_gecko/edit_molt/{gecko.id}/{molt.id}" #The feed_log's log id.
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Molt_Form(request.POST, request.FILES, instance=molt)
            print(request.FILES)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/profile/'+str(gecko.id))
        else:
            return HttpResponseRedirect('/leopard_gecko/profile/'+ str(gecko.id))
    else:
        form = Create_Molt_Form(instance=molt)
        print(form.fields)
        form.fields['gecko'].initial = gecko
        form.fields['log'].initial = molt.log

    return render(request, 'leo_log_form.html', {'tab_info': gecko.name + ' Molt log','form': form, 'gecko': gecko, 'user_info': request.user, 'endpoint': post_endpoint})


def add_gecko(request):
    """Add a gecko."""
    post_endpoint = f"/leopard_gecko/add_gecko"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Gecko_Form(request.POST, request.FILES)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/index')
        else:
            return HttpResponseRedirect('/leopard_gecko/index')
    else:
        form = Create_Gecko_Form()

    return render(request, 'leo_form.html', {'tab_info': ' Add New Gecko', 'form': form, 'user_info': request.user, 'endpoint': post_endpoint})


def edit_gecko(request, gecko):
    """Edit a gecko."""
    gecko = get_object_or_404(Gecko, id=gecko)
    post_endpoint = f"/leopard_gecko/edit_gecko/{gecko.id}"
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Gecko_Form(request.POST, request.FILES, instance=gecko)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/profile/' +str(gecko.id))
        else:
            return HttpResponseRedirect('/leopard_gecko/index')
    else:
        form = Create_Gecko_Form(instance=gecko)

    return render(request, 'leo_form.html', {'tab_info': gecko.name + ' Edit', 'form': form, 'user_info': request.user, 'endpoint': post_endpoint})


def tank_partial(request, gecko):
    """Gets logs for gecko, loads the logs partial."""
    gecko = get_object_or_404(Gecko, id=gecko)
    tank = get_object_or_404(Tank, gecko=gecko)
    tank_contents = tank.contents.all()
    tank_logs = Tank_Cleaning_Log.objects.filter(tank=tank).order_by('-date')
    log_count = tank_logs.count()

    context = {'user_info': request.user, 'gecko': gecko, 'tank': tank, 'logs': tank_logs, 'log_count': log_count, 'tank_contents': tank_contents}
    return render(request, 'leo_tank_partial.html', context)


def molt_partial(request, gecko):
    """Gets logs for gecko, loads the logs partial."""
    gecko = get_object_or_404(Gecko, id=gecko)
    molts = get_list_or_404(Molt.objects.order_by('-time'), gecko=gecko)

    context = {'user_info': request.user, 'gecko': gecko, 'molts': molts}
    return render(request, 'leo_molt_partial.html', context)


def gallery_partial(request, gecko):
    """Gets logs for gecko, loads the logs partial."""
    gecko = get_object_or_404(Gecko, id=gecko)
    pictures = get_list_or_404(Picture, gecko=gecko)

    context = {'user_info': request.user, 'gecko': gecko, 'pictures': pictures}
    return render(request, 'leo_gallery_partial.html', context)


def breeding_partial(request, gecko):
    """Gets logs for gecko, loads the logs partial."""
    gecko = get_object_or_404(Gecko, id=gecko)
    breeding_logs = get_list_or_404(Breeding_Log)

    context = {'user_info': request.user, 'gecko': gecko, 'breeding_logs': breeding_logs}
    return render(request, 'leo_breeding_partial.html', context)


def add_clean_log(request, tank):
    """Add a gecko."""
    post_endpoint = f"/leopard_gecko/add_clean_log/{tank}"
    tank = get_object_or_404(Tank, id=tank)
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Create_Tank_Cleaning_Log(request.POST)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/profile/' + str(tank.gecko.id))
        else:
            return HttpResponseRedirect('/leopard_gecko/profile/' + str(tank.gecko.id))
    else:
        form = Create_Tank_Cleaning_Log()
        form.fields['tank'].initial = tank

    return render(request, 'leo_log_form.html', {'tab_info': ' Add Cleaning Log', 'form': form, 'user_info': request.user, 'endpoint': post_endpoint})


def add_picture(request, gecko):
    """Add a gecko."""
    post_endpoint = f"/leopard_gecko/add_picture/{gecko}"
    gecko = get_object_or_404(Gecko, id=gecko)
    if request.method == 'POST':
        if request.user.is_superuser:
            form = Add_Picture_Form(request.POST, request.FILES)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/profile/' + str(gecko.id))
        else:
            return HttpResponseRedirect('/leopard_gecko/profile/' + str(gecko.id))
    else:
        form = Add_Picture_Form()
        form.fields['gecko'].initial = gecko

    return render(request, 'leo_log_form.html', {'tab_info': ' Add Cleaning Log', 'form': form, 'user_info': request.user, 'endpoint': post_endpoint})


def morph_index(request):
    morphs = Morph.objects.all()
    combo_morphs = Morph_Combo.objects.all()
    morphs_in_combos = {}
    for m in morphs:
        if combo_morphs.filter(morph=m).exists():
            print(m.morph_name)
            morph_combo_list = [
                combo_morphs.get(morph=m).first_req_morph.morph_name,
                combo_morphs.get(morph=m).second_req_morph.morph_name
            ]
            if combo_morphs.get(morph=m).third_req_morph:
                morph_combo_list.append(combo_morphs.get(morph=m).third_req_morph.morph_name)
            if combo_morphs.get(morph=m).fourth_req_morph:
                morph_combo_list.append(combo_morphs.get(morph=m).fourth_req_morph.morph_name)
            if combo_morphs.get(morph=m).fifth_req_morph:
                morph_combo_list.append(combo_morphs.get(morph=m).fifth_req_morph.morph_name)
            if combo_morphs.get(morph=m).sixth_req_morph:
                morph_combo_list.append(combo_morphs.get(morph=m).sixth_req_morph.morph_name)
            if combo_morphs.get(morph=m).seventh_req_morph:
                morph_combo_list.append(combo_morphs.get(morph=m).seventh_req_morph.morph_name)
            if combo_morphs.get(morph=m).eighth_req_morph:
                morph_combo_list.append(combo_morphs.get(morph=m).eighth_req_morph.morph_name)
            if combo_morphs.get(morph=m).ninth_req_morph:
                morph_combo_list.append(combo_morphs.get(morph=m).ninth_req_morph.morph_name)
            if combo_morphs.get(morph=m).tenth_req_morph:
                morph_combo_list.append(combo_morphs.get(morph=m).tenth_req_morph.morph_name)
            morphs_in_combos[m.id] = morph_combo_list

    print(morphs_in_combos)
    #print(morphs_in_combos['12303b17-f331-47ff-89ed-39d0b7d14348'].morph.morph_name)

    context = {'tab_info': 'Morph Index', 'morphs': morphs, 'combo_morphs': combo_morphs, 'user_info': request.user,
               'page_title': 'Leopard Gecko Morphs', 'morphs_in_combos': morphs_in_combos,
               'page_subtitle': f"Currently {morphs.count()} Known Morphs"
               }
    return render(request, 'leo_morphs_index.html', context)


def morph(request, morph):
    morph = get_object_or_404(Morph, id=morph)
    combo_morphs = {}
    try:
        combo_morphs = Morph_Combo.objects.get(morph=morph) or None
    except:
        pass
    geckos_with_morph = Gecko.objects.filter(morphs__id=morph.id)
    is_combo = {}
    if Morph_Combo.objects.filter(morph=morph).exists():
        is_combo = Morph_Combo.objects.filter(morph=morph)

    context = {'tab_info': morph.morph_name, 'morph': morph, 'combo_morphs': combo_morphs, 'user_info': request.user,
               'is_combo': is_combo, 'geckos_with_morph': geckos_with_morph}
    return render(request, 'leo_morph.html', context)


def add_measurement(request, gecko):
    gecko = get_object_or_404(Gecko, id=gecko)
    post_endpoint = f"/leopard_gecko/add_measurement/{gecko.id}"

    if request.method == 'POST':
        if request.user.is_superuser:
            form = Add_Measurement_Form(request.POST, request.FILES)
            if form.is_valid():
                # Process the data.
                # Just gonna save it for now without cleaning because I love me some technical debt.
                form.save()
                length = request.POST['length']
                weight = request.POST['weight']
                gecko.length = length
                gecko.weight = weight
                gecko.save()
                # Redirect
                return HttpResponseRedirect('/leopard_gecko/profile/' + str(gecko.id))
        else:
            return HttpResponseRedirect('/leopard_gecko/profile/' + str(gecko.id))
    else:
        form = Add_Measurement_Form()
        form.fields['gecko'].initial = gecko

    return render(request, 'leo_log_form.html',
                  {'tab_info': ' Add Measurement Log', 'form': form, 'user_info': request.user, 'endpoint': post_endpoint,
                   'page_title': f"Adding measurement for {gecko.name}"})