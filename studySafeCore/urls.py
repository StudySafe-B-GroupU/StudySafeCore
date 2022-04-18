from venv import create
import django
from django.urls import URLPattern, path 
from studySafeCore import views
from studySafeCore.venues_api_view import (delete_venue, list_all_venues, create_venue, view_venue, modify_venue, delete_venue)

urlpatterns = [
    path('hello', views.hello),
    path('api/venues', list_all_venues.as_view(), name='list_all_venues'),
    path('api/venues/create', create_venue.as_view(), name='create_venue'),
    path('api/venues/<int:id>', view_venue.as_view(), name='view_venue'),
    path('api/venues/modify/<int:id>', modify_venue.as_view(), name='modify_venue'),
    path('api/venues/delete/<int:id>', delete_venue.as_view(), name='delete_venue'),
]