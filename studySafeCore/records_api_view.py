from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Records
from .record_serializers import RecordsSerializer
from rest_framework import generics


class create_record(generics.CreateAPIView):
    serializer_class = RecordsSerializer
    def post(self, request, **kwargs):
        Records.objects.create( hku_id=request.data["hku_id"],venueCode=request.data["venueCode"],date=request.data["date"], time=request.data["time"])
        return Response("Successfully create a new record")
