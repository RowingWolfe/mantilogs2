from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('picture/<mantis_name>/<date>', views.picture, name='mantis-picture'),
    path('gallery/<mantis_name>', views.gallery, name='mantis-gallery'),
]
