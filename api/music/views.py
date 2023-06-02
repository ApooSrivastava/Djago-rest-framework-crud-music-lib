from django.shortcuts import render

# Create your views here.

#  we created the endpoint our app so in order to see the backend 
# have a face while we run the server using python3 manage.py runserver command
from rest_framework import generics
from .models import Songs
from .serializers import SongSerializer
class ListSongsView(generics.ListAPIView):
    

    queryset = Songs.objects.all()
    serializer_class = SongSerializer