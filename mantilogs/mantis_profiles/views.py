from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template.defaulttags import register
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, CreateView, UpdateView
from datetime import date, timedelta, datetime

#import datetime
import calendar
import time

import os

from .models import Mantis, Logs, Environment_Log, Gecko, Gecko_Morph, Gecko_Log, Culture, Culture_Log


# setup. Move this to settings and link to docs.
cam_options = '-ex night -awb tungsten -ifx denoise'


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    return HttpResponse("Mantis Profiles Hit!")

def log_env(request,temp,humidity):
    #Environment goodies.
    new_env_log = Environment_Log(
        humidity=humidity,
        temp=temp
    )
    new_env_log.save()
    return HttpResponse("Temp and humidity logged: " + temp + ' ' + humidity)



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
    # Select all logs where date - today <= 48 hours. Pass data along for each mantis.
    geckos = Gecko.objects.all()
    last_logs = {}
    for gecko in geckos:
        # Find logs for mantis
        if(Gecko_Log.objects.filter(gecko=gecko.name)):
            last_log[gecko.name] = Logs.objects.filter(
                gecko=gecko.name).latest('date')
        
     

    return render(request, 'gecko_index.html', {'geckos': geckos, 'last_logs': last_logs})
