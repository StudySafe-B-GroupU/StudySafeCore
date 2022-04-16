import django


from django.urls import URLPattern, path 
from studySafeCore import views
from studySafeCore.venuesAPI import (get_venue, create_venue, update_venue, modify_venue, delete_venue)

urlpatterns = [
    path('hello', views.hello),
    path('venues', get_venue),
    path('venues', create_venue)
]