#  serializers are used to convert complex data into python data types so that it can be further converted into JSON or XML.
from rest_framework import serializers
from .models import Songs

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", 'artist')