from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='gecko-index'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]