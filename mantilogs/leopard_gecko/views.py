from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
from django.template.defaulttags import register
from .models import Gecko, Log, Breeding_Log, Feeding_Log, Tank_Cleaning_Log, Molt, Clutch, Tank, Tank_Object, Death, Morph, Egg,Temperatures


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
                                                'page_subtitle': f"Currently {total_geckos} Geckos"})


def profile(request, gecko):
    """Gather all required info for the Gecko itself. Tabbed info will be in sub-views and ajaxed in."""
    gecko = get_object_or_404(Gecko, id=gecko)
    morphs = gecko.morphs.all()
    context = {'user_info': request.user, 'gecko': gecko, 'morphs': morphs}
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