from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Artist, Song
from ..serializers import SongSerializer
from ..views import SongView

fake = Faker()


class SongViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artist = Artist.objects.create()
        cls.songs = [
            Song.objects.create(
                title=fake.first_name(), artist=cls.artist, votes=fake.random_digit()
            )
            for _ in range(3)
        ]
        cls.song = cls.songs[0]

    def test_can_browse_all_songs(self):
        response = self.client.get(reverse('songs'))
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.songs), len(response.data))
        for song in self.songs:
            self.assertIn(SongSerializer(instance=song).data, response.data)

    def test_can_read_a_specific_song(self):
        response = self.client.get(reverse("songs/", args=[self.song.id]))
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(SongSerializer(instance=self.song).data, response.data)
