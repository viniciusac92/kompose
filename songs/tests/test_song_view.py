import songs
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Artist
from ..serializers import ArtistSerializer
from ..views import SongView

fake = Faker()


class SongViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artists = [Artist.objects.create(name=fake.first_name()) for _ in range(3)]
        cls.artist = cls.artists[0]

    def test_can_browse_all_artists(self):
        import ipdb

        ipdb.set_trace()
        response = self.client.get(Artist.get_absolute_url)
        import ipdb

        ipdb.set_trace()
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.artists), len(response.data))
        for person in self.artists:
            self.assertIn(ArtistSerializer(instance=person).data, response.data)
