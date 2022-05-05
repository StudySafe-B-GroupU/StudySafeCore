from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Records, HKUMembers, Venues
from .record_serializers import RecordsSerializer
from rest_framework import generics

class list_all_records(generics.ListAPIView):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer


class create_record(generics.CreateAPIView):
    serializer_class = RecordsSerializer
    def post(self, request, **kwargs):
        hku_id = HKUMembers.objects.get(hku_id=request.data["hku_id"])
        venueCode = Venues.objects.get(venueCode=request.data["venueCode"])
        Records.objects.create( hku_id=hku_id,venueCode=venueCode,event=request.data["event"],date_time=request.data["date_time"])
        return Response("Successfully create a new record")

