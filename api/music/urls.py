# we made this file in order to redirect the app to the main urls.py 
from django.urls import path 
from .views import ListSongsView

urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all")
]