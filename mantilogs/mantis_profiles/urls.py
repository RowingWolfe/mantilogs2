from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.mantis_list, name='index'),
    path('picture/<mantis_name>/<today>', views.picture, name='mantis-picture'),
    path('gallery/<mantis_name>', views.gallery, name='mantis-gallery'),
    path('profile/<mantis_name>', views.profile, name="mantis-profile"),
    path('deadn/', views.mantis_list_dead_naturally,
         name="mantis-list-dead-natural"),
    path('deadu/', views.mantis_list_dead_unknown,
         name="mantis-list-dead-unknown"),
    path('alive/', views.mantis_list_alive,
         name="mantis-list-alive"),
    path('crisis/', views.mantis_list_crisis,
         name="mantis-list-crisis"),
    path('feed/', views.mantis_list_feed,
         name="mantis-list-feed"),
    path('', views.mantis_list, name="mantis-list"),
]
