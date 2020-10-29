from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='inv-idx'),
    path('add_item/', views.add_item, name='add-item'),
    path('add_order/', views.add_order, name='add-order'),
    path('update_inventory', views.update_inventory, name='update-inv'),
    path('add_expiration_date/<item>', views.add_expiration_date, name='add-exp'),
    path('item_expired/<item>', views.item_expired, name='item-exp'),
    path('item_used/<item>', views.item_used, name='item-used'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]