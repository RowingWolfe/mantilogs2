from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import date
import calendar
import time

import os

from .models import Mantis, Logs


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
    ts = calendar.timegm(time.gmtime())
    today = str(ts)
    directory = './mantis_profiles/static/' + mantis_name
    mantis_data = Mantis.objects.get(name=mantis_name)
    logs = Logs.objects.filter(mantis=mantis_name).order_by('-date')
    picture_gallery = []

    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            picture_gallery.append('/static/'+mantis_name+'/'+filename)

    profile_picture = picture_gallery[0]

    return render(request, 'profile.html', {"mantis_data": mantis_data,  "logs": logs, "date": today, "profile_picture": profile_picture, "gallery": picture_gallery})


def mantis_list(request):
    mantids = Mantis.objects.all()
    return render(request, 'mantislist.html', {'mantids': mantids})
