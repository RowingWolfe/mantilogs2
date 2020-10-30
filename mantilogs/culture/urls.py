from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('index/', views.culture_index, name='index'),
    path('profile/<cul>/', views.culture_profile, name='culture-prof'),
    path('add_log/<cul>', views.add_log, name='add-culture-log'),
    path('edit_log/<cul>/<log>', views.edit_log, name='edit-culture-log'),
    path('add_culture/', views.add_culture, name='add-culture'),
    path('edit_culture/<cul>', views.edit_culture, name='edit-culture'),
    path('add_quarantine/<cul>', views.add_quarantine, name='add-quarantine'),
    path('edit_quarantine/<quar>', views.edit_quarantine, name='edit-quarantine'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
