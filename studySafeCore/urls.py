from venv import create
import django
from django.urls import URLPattern, path 
from studySafeCore import views
from studySafeCore.venues_api_view import (delete_venue, list_all_venues, create_venue, view_venue, modify_venue, delete_venue)
from studySafeCore.HKUmembers_api_view import (create_hkumembers, list_all_hkumembers, view_hkumembers, modify_hkumembers, delete_hkumembers)
from studySafeCore.records_api_view import (list_all_records,create_record)

urlpatterns = [
    path('hello', views.hello),
    path('api/venues', list_all_venues.as_view(), name='list_all_venues'),
    path('api/venues/create', create_venue.as_view(), name='create_venue'),
    path('api/venues/<str:venueCode>', view_venue.as_view(), name='view_venue'),
    path('api/venues/modify/<int:id>', modify_venue.as_view(), name='modify_venue'),
    path('api/venues/delete/<int:id>', delete_venue.as_view(), name='delete_venue'),

    path('api/hkumembers', list_all_hkumembers.as_view(), name='list_all_hkumembers'),
    path('api/hkumembers/create', create_hkumembers.as_view(), name='create_hkumembers'),
    path('api/hkumembers/<int:id>', view_hkumembers.as_view(), name='view_hkumembers'),
    path('api/hkumembers/modify/<int:id>', modify_hkumembers.as_view(), name='modify_hkumembers'),
    path('api/hkumembers/delete/<int:id>', delete_hkumembers.as_view(), name='delete_hkumembers'),
    
    path('api/records', list_all_records.as_view(), name="list_all_records"),
    path('api/records/create', create_record.as_view(), name='create_record'),
]
