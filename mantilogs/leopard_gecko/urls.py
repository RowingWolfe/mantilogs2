from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='gecko-index'),
    path('profile/<gecko>', views.profile, name='gecko-prof'),
    path('info_partial/<gecko>', views.info_partial, name='info-partial'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]