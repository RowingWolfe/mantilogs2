from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import register
from django.http import HttpResponse
from datetime import date, timedelta
import datetime
import calendar
import time

import os

from .models import Mantis, Logs


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    return HttpResponse("Mantis Profiles Hit!")
# Create your views here.


def picture(request, mantis_name, today):
    if not os.path.exists("./mantis_profiles/static/" + mantis_name):
        os.system('mkdir ./mantis_profiles/static/' + mantis_name)
    image = './mantis_profiles/static/{0}/{1}.jpg'.format(
        mantis_name, today)
    print(image)
    os.system('raspistill -o ' + image)
    # TODO: Add button to mantis log entry to fire this endpoint.
    # TODO: Add View templates.
    profile_pic_to_change = Mantis.objects.get(name=mantis_name)
    profile_pic_to_change.profile_pic = '/static/{0}/{1}.jpg'.format(
        mantis_name, today)
    profile_pic_to_change.save()
    return HttpResponse("Picture taken: %s" % mantis_name + '/' + today + '.jpg')


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
    mantids = Mantis.objects.all()
    logs_last_48 = {}
    crisis_last_48 = {}
    last_fed = {}
    filtered_mantids = {}
    for mantis in mantids:
        # Find logs for mantis
        if(Logs.objects.filter(mantis=mantis.name)):
            logs_last_48[mantis.name] = Logs.objects.filter(
                mantis=mantis.name).latest('date')
            crisis_last_48[mantis.name] = logs_last_48[mantis.name].crisis_today
        if Logs.objects.filter(mantis=mantis.name).filter(fed_today=True):
            last_fed[mantis.name] = Logs.objects.filter(
                mantis=mantis.name).filter(fed_today=True).latest('date').date
    for mantis in mantids:
        if crisis_last_48.__contains__(mantis.name):
            filtered_mantids[mantis.name] = mantis

    return render(request, 'mantislist.html', {'mantids': filtered_mantids, 'logs_last_48': logs_last_48, 'crisis_last_48': crisis_last_48, 'last_fed': last_fed, })


def mantis_list_feed(request):
    # Select all logs where date - today <= 48 hours. Pass data along for each mantis.
    mantids = Mantis.objects.all()
    mantis_logs = Logs.objects.filter(fed_today=True)
    filtered_mantids = mantids.filter(
        mantis=mantis_logs.mantis)
    logs_last_48 = {}
    crisis_last_48 = {}
    last_fed = {}
    print(filtered_mantids)
    # for mantis in mantids:
    #     # Find logs for mantis
    #     if(Logs.objects.filter(mantis=mantis.name)):
    #         logs_last_48[mantis.name] = Logs.objects.filter(
    #             mantis=mantis.name).latest('date')
    #         crisis_last_48[mantis.name] = logs_last_48[mantis.name].crisis_today
    #     if Logs.objects.filter(mantis=mantis.name).filter(fed_today=True):
    #         last_fed[mantis.name] = Logs.objects.filter(
    #             mantis=mantis.name).filter(fed_today=True).latest('date').date

    return render(request, 'mantislist.html', {'mantids': filtered_mantids, 'logs_last_48': logs_last_48, 'crisis_last_48': crisis_last_48, 'last_fed': last_fed, })


# def mantis_list_feed(request):
#     # Select all logs where date - today <= 48 hours. Pass data along for each mantis.
#     mantids = Mantis.objects.filter()
#     logs_last_48 = {}
#     crisis_last_48 = {}
#     last_fed = {}
#     filtered_mantids = {}
#     for mantis in mantids:
#         # Find logs for mantis

#         if Logs.objects.filter(mantis=mantis.name).filter(fed_today=True):
#             last_fed[mantis.name] = Logs.objects.filter(
#                 mantis=mantis.name).filter(fed_today=True).latest('date').date
#             if last_fed[mantis.name]:
#                 print(last_fed[mantis.name])
#                 print(datetime.date.today())
#                 d0 = last_fed[mantis.name]
#                 d1 = datetime.date.today()
#                 delta = d1 - d0
#                 days_since_fed = delta.days
#                 if days_since_fed > 2:
#                     filtered_mantids[mantis.name] = mantids[mantis].values()
#                     if(filtered_mantids[mantis.name]):
#                         logs_last_48[mantis.name] = Logs.objects.filter(
#                             mantis=mantis.name).latest('date')
#                         crisis_last_48[mantis.name] = logs_last_48[mantis.name].crisis_today
#                         print(filtered_mantids)
#                         print(mantids)

#     return render(request, 'mantislist.html', {'mantids': filtered_mantids, 'logs_last_48': logs_last_48, 'crisis_last_48': crisis_last_48, 'last_fed': last_fed, })
