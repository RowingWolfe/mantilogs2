from django.shortcuts import render
from django.http import HttpResponse
import os


def index(request):
    return HttpResponse("Mantis Profiles Hit!")
# Create your views here.


def picture(request, mantis_name, date):
    if not os.path.exists("./static/" + mantis_name):
        os.system('mkdir ./static/' + mantis_name)
    # if not os.path.exists("./static/" + mantis_name + '/' + date):
    #     os.system('mkdir ./static/' + mantis_name + '/' + date)

    image = './static/{0}/{0}_{1}.jpg'.format(mantis_name, date)
    os.system('raspistill -o ' + image)
    return HttpResponse("Picture taken: %s." % mantis_name + date + ' || ' + image)


def gallery(request, mantis_name):
    # Display gallery for mantis.
    pass
