from django.urls import path, include
from . import views

urlpatterns = [
    path('gecko/', views.gecko_calc,name='gecko_calc'),
    path('gecko_partial/<gecko1>/<gecko2>', views.gecko_partial, name='gecko_partial'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]