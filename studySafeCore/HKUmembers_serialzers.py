from sre_constants import MAX_UNTIL
from rest_framework import serializers

class HkuMembersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    hku_id = serializers.CharField(max_length = 10)
    name = serializers.CharField(max_length = 150)