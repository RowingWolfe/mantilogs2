from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Mantis Profiles Hit!")
# Create your views here.
