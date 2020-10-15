from django.urls import path, include

from . import views
urlpatterns = [
    path('index/', views.culture_index, name='index'),
    path('<cul>/', views.culture_profile, name='culture-prof'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]