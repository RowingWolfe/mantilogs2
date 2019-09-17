from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('', views.mantis_list, name='index'),
    path('picture/<mantis_name>/<today>', views.picture, name='mantis-picture'),
    path('gallery/<mantis_name>', views.gallery, name='mantis-gallery'),
    path('profile/<mantis_name>', views.profile, name="mantis-profile"),
    path('/', views.mantis_list, name="mantis-list"),
]
