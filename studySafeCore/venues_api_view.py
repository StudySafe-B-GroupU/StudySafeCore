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
    queryset = Venues.objects.all()
    serializer_class = VenuesSerializer


class view_venue(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = VenuesSerializer

    def get_queryset(self, **kwargs):
        venue_id = self.kwargs['id']
        return Venues.objects.filter(id=venue_id)


class modify_venue(generics.UpdateAPIView):
    lookup_field = 'id'
    serializer_class = VenuesSerializer

    def get_queryset(self, **kwargs):
        uid = self.kwargs['uid']
        queryset = HKUMember.objects.filter(uid=uid)
        return queryset


class delete_venue(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = VenuesSerializer

    def get_queryset(self, **kwargs):
        venue_id = self.kwargs['id']
        return Venues.objects.filter(id=venue_id)