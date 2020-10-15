from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template.defaulttags import register
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, CreateView, UpdateView
from datetime import date, timedelta, datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#from .forms import Add_Culture_Log


#TODO: Abstract filters from the views, shit's getting ugly.

#import datetime
import calendar
import time
import os
from .models import Mantis, Logs, Environment_Log, Gecko, Gecko_Morph, Gecko_Log, Culture, Culture_Log

from .tools import get_last_vitd, get_last_multivit, get_last_tank_clean, get_last_fed, get_last_defecation


# setup. Move this to settings and link to docs.
cam_options = '-ex night -awb tungsten -ifx denoise'


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    return HttpResponse("Mantis Profiles Hit!")

def dashboard(request):
    userinfo = {}
    if request.user.is_authenticated:
        userinfo = request.user
    context={'info':'Nothing yet.', 'user_info': userinfo}
    return render(request, 'dashboard.html', context)

def log_env(request,temp,humidity, location):
    #Environment goodies.
    new_env_log = Environment_Log(
        humidity=humidity,
        temp=temp,
        location=location
    )
    new_env_log.save()
    return HttpResponse("Temp and humidity logged: " + temp + ' ' + humidity + ' in ' + location)



def picture(request, mantis_name, today):
    if not os.path.exists("./mantis_profiles/static/" + mantis_name):
        os.system('mkdir ./mantis_profiles/static/' + mantis_name)
    image = './mantis_profiles/static/{0}/{1}.jpg'.format(
        mantis_name, today)
    print(image)
    os.system('raspistill -o ' + image + ' '+cam_options)
    # TODO: Add button to mantis log entry to fire this endpoint.
    # TODO: Add View templates.
    profile_pic_to_change = Mantis.objects.get(name=mantis_name)
    pic_location = '/static/{0}/{1}.jpg'.format(
        mantis_name, today)
    profile_pic_to_change.profile_pic = pic_location
    profile_pic_to_change.save()
    return HttpResponse("Picture taken: %s" % mantis_name + '/' + today + '.jpg' + '<img src="{0}">'.format(pic_location))


def gallery(request, mantis_name):
    # Display gallery for mantis.
    images = []
    directory = './mantis_profiles/static/'+mantis_name
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            # Add by picture date, for now be lazy.
            images.append('/'+mantis_name+'/'+filename)
    context = {
        'mantis_name': mantis_name,
        'images': images,
        'directory': mantis_name + '/',

    }
    return render(request, 'gallery.html', context)


def profile(request, mantis_name):
    # Need to check for gallery folder here to prevent fuuuucking stupidity.

    ts = calendar.timegm(time.gmtime())
    today = str(ts)
    directory = './mantis_profiles/static/' + mantis_name
    # Do the check, man.
    if not os.path.exists(directory):
        os.system('mkdir '+directory)

    mantis_data = Mantis.objects.get(name=mantis_name)
    logs = Logs.objects.filter(mantis=mantis_name).order_by('-date')
    picture_gallery = []

    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            picture_gallery.append('/static/'+mantis_name+'/'+filename)

    profile_picture = ''
    if len(picture_gallery) > 0:
        try:
            profile_picture = picture_gallery[0]
        except (FileNotFoundError):
            print("No pictures.")
    else:
        profile_picture = '/static/mantis_riding_snake1.jpg'

    return render(request, 'profile.html', {"mantis_data": mantis_data,  "logs": logs, "date": today, "profile_picture": profile_picture, "gallery": picture_gallery})


def mantis_list(request):
    # Select all logs where date - today <= 48 hours. Pass data along for each mantis.
    mantids = Mantis.objects.all()
    logs_last_48 = {}
    crisis_last_48 = {}
    last_fed = {}
    for mantis in mantids:
        # Find logs for mantis
        if(Logs.objects.filter(mantis=mantis.name)):
            logs_last_48[mantis.name] = Logs.objects.filter(
                mantis=mantis.name).latest('date')
            crisis_last_48[mantis.name] = logs_last_48[mantis.name].crisis_today
        if Logs.objects.filter(mantis=mantis.name).filter(fed_today=True):
            last_fed[mantis.name] = Logs.objects.filter(
                mantis=mantis.name).filter(fed_today=True).latest('date').date

    return render(request, 'mantislist.html', {'mantids': mantids, 'logs_last_48': logs_last_48, 'crisis_last_48': crisis_last_48, 'last_fed': last_fed, })


def mantis_list_dead_naturally(request):
    # Select all logs where date - today <= 48 hours. Pass data along for each mantis.
    mantids = Mantis.objects.all().filter(died_natural=True)
    logs_last_48 = {}
    crisis_last_48 = {}
    last_fed = {}
    for mantis in mantids:
        # Find logs for mantis
        if(Logs.objects.filter(mantis=mantis.name)):
            logs_last_48[mantis.name] = Logs.objects.filter(
                mantis=mantis.name).latest('date')
            crisis_last_48[mantis.name] = logs_last_48[mantis.name].crisis_today
        if Logs.objects.filter(mantis=mantis.name).filter(fed_today=True):
            last_fed[mantis.name] = Logs.objects.filter(
                mantis=mantis.name).filter(fed_today=True).latest('date').date

    return render(request, 'mantislist.html', {'mantids': mantids, 'logs_last_48': logs_last_48, 'crisis_last_48': crisis_last_48, 'last_fed': last_fed, })


def mantis_list_dead_unknown(request):
    # Select all logs where date - today <= 48 hours. Pass data along for each mantis.
    mantids = Mantis.objects.all().filter(died_unknown=True)
    logs_last_48 = {}
    crisis_last_48 = {}
    last_fed = {}
    for mantis in mantids:
        # Find logs for mantis
        if(Logs.objects.filter(mantis=mantis.name)):
            logs_last_48[mantis.name] = Logs.objects.filter(
                mantis=mantis.name).latest('date')
            crisis_last_48[mantis.name] = logs_last_48[mantis.name].crisis_today
        if Logs.objects.filter(mantis=mantis.name).filter(fed_today=True):
            last_fed[mantis.name] = Logs.objects.filter(
                mantis=mantis.name).filter(fed_today=True).latest('date').date

    return render(request, 'mantislist.html', {'mantids': mantids, 'logs_last_48': logs_last_48, 'crisis_last_48': crisis_last_48, 'last_fed': last_fed, })


def mantis_list_alive(request):
    # Select all logs where date - today <= 48 hours. Pass data along for each mantis.
    mantids = Mantis.objects.all().filter(
        died_unknown=False).filter(died_natural=False)
    logs_last_48 = {}
    crisis_last_48 = {}
    last_fed = {}
    for mantis in mantids:
        # Find logs for mantis
        if(Logs.objects.filter(mantis=mantis.name)):
            logs_last_48[mantis.name] = Logs.objects.filter(
                mantis=mantis.name).latest('date')
            crisis_last_48[mantis.name] = logs_last_48[mantis.name].crisis_today
        if Logs.objects.filter(mantis=mantis.name).filter(fed_today=True):
            last_fed[mantis.name] = Logs.objects.filter(
                mantis=mantis.name).filter(fed_today=True).latest('date').date

    return render(request, 'mantislist.html', {'mantids': mantids, 'logs_last_48': logs_last_48, 'crisis_last_48': crisis_last_48, 'last_fed': last_fed, })


def mantis_list_crisis(request):
    # Select all logs where date - today <= 48 hours. Pass data along for each mantis.
    living_mantids = Mantis.objects.filter(
        died_unknown=False, died_natural=False)
    print(living_mantids)
    logs_last_48 = {}
    crisis_last_48 = {}
    last_fed = {}
    all_good_here = ''
    # For each mantis

    filtered_mantids = []
    for mantis in living_mantids:
        # Get last log of mantis where fed_today=true
        try:
            if not mantis in filtered_mantids:
                if Logs.objects.filter(mantis=mantis, crisis_today=True).latest('date'):
                    last_log = Logs.objects.filter(
                        mantis=mantis, crisis_today=True).latest('date')
                # Add mantis to some data struct that can have no duplicate vals
                # TODO: Do that thing with the data structures, this is cheap.
                    if not last_log.mantis in filtered_mantids:
                        filtered_mantids.append(last_log.mantis)
                        last_fed[mantis.name] = last_log.date
                        print(last_log.mantis)
        except ObjectDoesNotExist:
            pass

    if not len(filtered_mantids):
        all_good_here = "Everything seems fine. You should probably panic."

    return render(request, 'mantislist.html', {'mantids': filtered_mantids, 'logs_last_48': logs_last_48, 'crisis_last_48': crisis_last_48, 'last_fed': last_fed, 'all_good': all_good_here, })


def mantis_list_feed(request):
    # TODO: FIx me
    # Select all logs where date - today <= 48 hours. Pass data along for each mantis.
    # You only need the logs, dummy.
    living_mantids = Mantis.objects.filter(
        died_unknown=False, died_natural=False)
    print(living_mantids)
    logs_last_48 = {}
    crisis_last_48 = {}
    last_fed = {}
    all_good_here = ''
    # For each mantis

    filtered_mantids = []
    for mantis in living_mantids:
        # Get last log of mantis where fed_today=true
        try:
            if not mantis in filtered_mantids:
                if Logs.objects.filter(mantis=mantis, fed_today=True).latest('date'):
                    last_log = Logs.objects.filter(
                        mantis=mantis, fed_today=True).latest('date')
                # Add mantis to some data struct that can have no duplicate vals
                # TODO: Do that thing with the data structures, this is cheap.
                    if not last_log.mantis in filtered_mantids:
                        # Check if log date's delta is more than 3 from today.
                        time_since_fed = datetime.now().date() - last_log.date
                        if time_since_fed.days > 2:
                            filtered_mantids.append(last_log.mantis)
                            
                            last_fed[mantis.name] = last_log.date
                            print(last_log.mantis)
        except ObjectDoesNotExist:
            pass

    if not len(filtered_mantids):
        all_good_here = "Everything seems fine. You should probably panic."

    return render(request, 'mantislist.html', {'mantids': filtered_mantids, 'logs_last_48': logs_last_48, 'crisis_last_48': crisis_last_48, 'last_fed': last_fed, 'all_good': all_good_here, })


def gecko_list(request):
    # Select all logs where date - today <= 48 hours. Pass data along for each gecko
    geckos = Gecko.objects.all()
    last_logs = {}
    last_vitd = {}
    last_multivit = {}
    last_tank_clean = {}
    last_fed = {}
    last_defecated = {}
    for gecko in geckos:
        # Find logs for gecko
        if(Gecko_Log.objects.filter(gecko=gecko.name)):
            last_logs[gecko.name] = Gecko_Log.objects.filter(
                gecko=gecko.name).latest('date')

        last_multivit[gecko.name] = get_last_multivit(gecko)
        last_vitd[gecko.name] = get_last_vitd(gecko)
        last_tank_clean[gecko.name] = get_last_tank_clean(gecko)
        last_fed[gecko.name] = get_last_fed(gecko)
        last_defecated[gecko.name] = get_last_defecation(gecko)


    return render(request, 'gecko_index.html', {'geckos': geckos, 'last_logs': last_logs,
        'last_multivit': last_multivit, 'last_vitd': last_vitd, 'last_tank_clean': last_tank_clean,
                                                "last_defecation": last_defecated, "last_fed": last_fed})

def gecko_profile(request, gecko_name):
    gecko_data = Gecko.objects.get(name=gecko_name)
    logs = Gecko_Log.objects.filter(gecko=gecko_name).order_by('-date')

    return render(request, 'gecko_profile.html', {"gecko": gecko_data,  "all_logs": logs})



def culture_list(request):
    # Select all logs where date - today <= 48 hours. Pass data along for each Culture.
    cultures = Culture.objects.all()
    last_logs = {}
    for culture in cultures:
        # Find logs for Culture
        # TODO: invalid literal for int() with base 10: 'Cricket Grandaddy Culture'
        if(Culture_Log.objects.filter(culture=culture)):
            last_logs[culture] = Culture_Log.objects.filter(
                culture=culture).latest('date')

    return render(request, 'culture_index.html', {'cultures': cultures, 'last_logs': last_logs})

def culture_profile(request, culture_name):
    culture_data = Culture.objects.get(culture_name=culture_name)
    logs = Culture_Log.objects.filter(culture=culture_data).order_by('-date')

    return render(request, 'culture_profile.html', {"culture": culture_data,  "all_logs": logs})

# @login_required
# def add_culture_log(request, culture_name):
#     """Should render a form for adding a log to culture where <culture_name> is the Culture to add the log to."""
#     #culture = get_object_or_404(Culture, culture_name)
#     if request.user.is_authenticated and request.user.is_superuser:
#         if request.method == 'POST':
#             form = Add_Culture_Log(request.POST)
#             if form.is_valid():
#                 print("Form validated.")
#         elif request.method == 'GET':
#             return render(request, 'culture_log_form.html', {'culture_name': culture_name, 'user':request.user})
#     else:
#         return redirect('/')

