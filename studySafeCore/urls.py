import django


from django.urls import URLPattern, path 
from studySafeCore import views

urlpatterns = [
    path('hello', views.hello),
]