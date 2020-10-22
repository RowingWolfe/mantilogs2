from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='gecko-index'),
    path('profile/<gecko>', views.profile, name='gecko-prof'),
    path('info_partial/<gecko>', views.info_partial, name='info-partial'),
    path('log_partial/<log>', views.log_partial, name='log-partial'),
    path('logs_partial/<gecko>', views.logs_partial, name='logs-partial'),
    path('add_log/<gecko>', views.add_log, name='add-log-form'),
    path('edit_log/<gecko>/<log>', views.edit_log, name='edit-log-form'),
    path('add_feed_log/<gecko>/<log>', views.add_feed_log, name='add-fd-log-form'),
    path('edit_feed_log/<gecko>/<log>', views.edit_feed_log, name='edit-fd-log-form'),
    path('add_molt/<gecko>/<log>', views.add_molt, name='add-molt-form'),
    path('edit_molt/<gecko>/<log>', views.edit_molt, name='edit-molt-form'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]