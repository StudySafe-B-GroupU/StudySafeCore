from urllib import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HKUMembers
from .HKUmembers_serialzers import HkuMembersSerializer
from rest_framework import generics

class create_hkumembers(generics.CreateAPIView):
    serializer_class = HkuMembersSerializer
    print(request)
    def post(self, request, **kwargs):
        HKUMembers.objects.create(hku_id=request.data["hku_id"], name=request.data["name"])
        return Response("Successfully create a new record")

class list_all_hkumembers(generics.ListAPIView):
    queryset = HKUMembers.objects.all()
    serializer_class = HkuMembersSerializer

class view_hkumembers(generics.RetrieveAPIView):
    lookup_field = 'hku_id'
    serializer_class = HkuMembersSerializer
    def get_queryset(self, **kwargs):
        hku_id = self.kwargs['hku_id']
        return HKUMembers.objects.filter(hku_id=hku_id)

class modify_hkumembers(generics.UpdateAPIView):
    lookup_field = 'hku_id'
    serializer_class = HkuMembersSerializer
    def update(self, request, **kwargs):
        hku_id = self.kwargs['hku_id']
        HKUMembers.objects.filter(hku_id=hku_id).update(name=request.data["name"])
        return Response("Successsfully update a record")

class delete_hkumembers(generics.DestroyAPIView):
    lookup_field = 'hku_id'
    serializer_class = HkuMembersSerializer
    def destroy(self,request, **kwargs): 
        hku_id = self.kwargs['hku_id']
        HKUMembers.objects.filter(id=hku_id).delete()
        return Response("Sucessfully delete a record")