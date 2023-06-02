# from django.test import TestCase

# Create your tests here.
# we created this file for test runs before running the server.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    def setUp(self):
        self.create_song("like_glue", "sean paul") 
        self.create_song("simple_song", "konshens")
        self.create_song("love os wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")

class GetAllSongsTest(BaseViewTest):
    def test_get_all_songs(self):
        response = self.client.get(
            reverse("songs-all", kwargs={"version":"v1"})

        )
        expected = Songs.objects.all()
        serialized = SongSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status, status.HTTP_200_OK)
