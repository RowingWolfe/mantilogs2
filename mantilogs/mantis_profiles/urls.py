from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.dashboard, name='index'),
    path('picture/<mantis_name>/<today>', views.picture, name='mantis-picture'),
    path('gallery/<mantis_name>', views.gallery, name='mantis-gallery'),
    path('mantis/profile/<mantis_name>', views.profile, name="mantis-profile"),
    path('mantis/deadn/', views.mantis_list_dead_naturally,
         name="mantis-list-dead-natural"),
    path('mantis/deadu/', views.mantis_list_dead_unknown,
         name="mantis-list-dead-unknown"),
    path('mantis/alive/', views.mantis_list_alive,
         name="mantis-list-alive"),
    path('mantis/crisis/', views.mantis_list_crisis,
         name="mantis-list-crisis"),
    path('mantis/feed/', views.mantis_list_feed,
         name="mantis-list-feed"),
    path('newenvlog/<temp>/<humidity>', views.log_env, name='env-log'),
    path('geckos/index', views.gecko_list, name="gecko-list"),
    path('geckos/profile/<gecko_name>', views.gecko_profile, name='gecko-profile'),
    path('cultures/index', views.culture_list, name="culture-list"),
    path('cultures/profile/<culture_name>', views.culture_profile, name='culture-profile'),
    path('', views.mantis_list, name="mantis-list"),
]
