from sre_constants import MAX_UNTIL
from rest_framework import serializers

class RecordsSerializer(serializers.Serializer):
    id  =serializers.IntegerField(read_only =True)
    hku_id = serializers.CharField(max_length = 10)
    venueCode = serializers.CharField(max_length = 200)
    date_time = serializers.DateTimeField()
