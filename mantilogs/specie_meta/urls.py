from django.urls import path, include

from . import views
urlpatterns = [

]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]