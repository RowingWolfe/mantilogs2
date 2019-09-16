from django.shortcuts import render
from django.http import HttpResponse
import os


def index(request):
    return HttpResponse("Mantis Profiles Hit!")
# Create your views here.


def picture(request, mantis_name, date):
    if not os.path.exists("./mantis_profiles/static/" + mantis_name):
        os.system('mkdir ./mantis_profiles/static/' + mantis_name)
    # if not os.path.exists("./static/" + mantis_name + '/' + date):
    #     os.system('mkdir ./static/' + mantis_name + '/' + date)

    image = './mantis_profiles/static/{0}/{0}_{1}.jpg'.format(mantis_name, date)
    os.system('raspistill -o ' + image)
    # TODO: Add button to mantis log entry to fire this endpoint.
    # TODO: Add View templates.
    return HttpResponse("Picture taken: %s." % mantis_name + date + ' || ' + image)


def gallery(request, mantis_name):
    # Display gallery for mantis.
    images = []
    directory = './mantis_profiles/static/'+mantis_name
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            #Add by picture date, for now be lazy.
            images.append('/'+mantis_name+'/'+filename)
    context={
        'mantis_name': mantis_name,
        'images': images,
        'directory': mantis_name + '/' ,

    }
    return render(request, 'gallery.html', context)
