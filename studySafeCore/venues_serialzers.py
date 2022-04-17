from sre_constants import MAX_UNTIL
from rest_framework import serializers

class VenuesSerializer(serializers.Serializer):
    id  =serializers.IntegerField(read_only =True)
    venueCode = serializers.CharField(max_length = 200)
    location = serializers.CharField(max_length = 150)
    type = serializers.CharField(max_length = 2)
    capacity = serializers.IntegerField()