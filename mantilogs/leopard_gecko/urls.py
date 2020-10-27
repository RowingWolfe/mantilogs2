from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='landing'),
    path('index/', views.index, name='gecko-index'),
    path('profile/<gecko>', views.profile, name='gecko-prof'),
    path('info_partial/<gecko>', views.info_partial, name='info-partial'),
    path('log_partial/<log>', views.log_partial, name='log-partial'),
    path('tank_partial/<gecko>', views.tank_partial, name='tank-partial'),
    path('molt_partial/<gecko>', views.molt_partial, name='molt-partial'),
    path('gallery_partial/<gecko>', views.gallery_partial, name='gallery-partial'),
    path('breeding_partial/<gecko>', views.breeding_partial, name='breeding-partial'),
    path('logs_partial/<gecko>', views.logs_partial, name='logs-partial'),
    path('add_log/<gecko>', views.add_log, name='add-log-form'),
    path('edit_log/<gecko>/<log>', views.edit_log, name='edit-log-form'),
    path('add_feed_log/<gecko>/<log>', views.add_feed_log, name='add-fd-log-form'),
    path('edit_feed_log/<gecko>/<log>', views.edit_feed_log, name='edit-fd-log-form'),
    path('add_molt/<gecko>/<log>', views.add_molt, name='add-molt-form'),
    path('add_clean_log/<tank>', views.add_clean_log, name='add-clean-form'),
    path('edit_molt/<gecko>/<log>', views.edit_molt, name='edit-molt-form'),
    path('add_gecko', views.add_gecko, name='add-gecko-form'),
    path('add_picture/<gecko>', views.add_picture, name='add-picture-form'),
    path('edit_gecko/<gecko>', views.edit_gecko, name='edit-gecko-form'),
    path('morphs', views.morph_index, name='morphs-index'),
    path('morph/<morph>', views.morph, name='morph'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]