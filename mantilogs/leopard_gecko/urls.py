from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.culture_index, name='index'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]