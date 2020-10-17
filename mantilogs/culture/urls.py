from django.urls import path, include

from . import views
urlpatterns = [
    path('index/', views.culture_index, name='index'),
    path('<cul>/', views.culture_profile, name='culture-prof'),
    path('<cul>/add_log', views.add_log, name='add-culture-log'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]