from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Venues
from .venues_serialzers import VenuesSerializer
from rest_framework import generics

# @api_view(['GET'])
# def list_all_venues(request):
#     venues = Venues.objects.all()
#     venues_serializer = VenuesSerializer(venues, many=True)
#     return Response(venues_serializer.data)


# @api_view(['POST'])
# def create_venues(request):
#     return


# @api_view(['GET'])
# def view_venues(self,):
#     venue_id = self.kwargs[venue_id]
#     venues = Venues.objects.get(id=venue_id)
#     venues_serializer = VenuesSerializer(venues, many=True)
#     return Response(venues_serializer.data)


# @api_view(['PUT'])
# def modify_venues(request):
#     return


# @api_view(['DELETE'])
# def delete_venues(request):
#     return

class list_all_venues(generics.ListAPIView):
    queryset = Venues.objects.all()
    serializer_class = VenuesSerializer


class create_venue(generics.CreateAPIView):
    serializer_class = VenuesSerializer
    def post(self, request, **kwargs):
        # venueCode = self.kwargs['venueCode']
        # location = self.kwargs['location']
        # type = self.kwargs['type']
        # capacity = self.kwargs['capacity']
        # Venues.objects.create(venueCode=venueCode, location=location, type=type, capacity=capacity)
        Venues.objects.create(venueCode=request.data["venueCode"], location=request.data["location"], type=request.data["type"], capacity=request.data["capacity"])
        return Response("Successfully create a new record")

class view_venue(generics.RetrieveAPIView):
    lookup_field = 'venueCode'
    serializer_class = VenuesSerializer
    def get_queryset(self, **kwargs):
        venueCode = self.kwargs['venueCode']
        return Venues.objects.filter(venueCode=venueCode)


class modify_venue(generics.UpdateAPIView):
    lookup_field = 'venueCode'
    serializer_class = VenuesSerializer
    def update(self, request, **kwargs):
        venueCode = self.kwargs['venueCode']
        Venues.objects.filter(id=venueCode).update(location=request.data["location"], type=request.data["type"], capacity=request.data["capacity"])
        return Response("Successsfully update a record")

class delete_venue(generics.DestroyAPIView):
    lookup_field = 'venueCode'
    serializer_class = VenuesSerializer
    def destroy(self,request, **kwargs): 
        venueCode = self.kwargs['venueCode']
        Venues.objects.filter(id=venueCode).delete()
        return Response("Sucessfully delete a record")