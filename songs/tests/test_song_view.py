import json

from django.forms.fields import JSONString
from django.http import JsonResponse
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
        response = self.client.get(reverse("songs"))
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.songs), len(response.data))
        for song in self.songs:
            self.assertIn(SongSerializer(instance=song).data, response.data)

    def test_can_read_a_specific_song(self):
        response = self.client.get(reverse("songs/", args=[self.song.id]))
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(SongSerializer(instance=self.song).data, response.data)

    def test_can_add_a_new_song(self):
        song = {"title": fake.first_name(), "artist": {"name": fake.first_name()}}
        response = self.client.post(
            reverse('songs'),
            data=json.dumps(song),
            content_type='application/json',
        )
        created_song = Song.objects.get(title=song["title"])
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        for key, value in song.items():
            if key != "artist":
                self.assertEquals(value, response.data[key])
                self.assertEquals(value, getattr(created_song, key))

            else:
                self.assertEquals(value['name'], response.data[key]['name'])
                self.assertEquals(
                    value['name'], getattr(created_song, key).__dict__['name']
                )

    def test_can_edit_a_song(self):
        artist = Artist.objects.create()
        song_data = {"title": fake.first_name(), "artist": artist}
        song = Song.objects.create(**song_data)
        song_edit = {"title": fake.first_name(), "artist": {"name": fake.first_name()}}
        response = self.client.put(
            reverse('songs/', args=[song.id]),
            data=json.dumps(song_edit),
            content_type='application/json',
        )
        song.refresh_from_db()
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        for key, value in song_edit.items():
            if key != "artist":
                self.assertEquals(value, response.data[key])
                self.assertEquals(value, getattr(song, key))

            else:
                self.assertEquals(value['name'], response.data[key]['name'])
                self.assertEquals(value['name'], getattr(song, key).__dict__['name'])

    def test_can_delete_a_song(self):
        response = self.client.delete(reverse('songs/', args=[self.song.id]))
        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertFalse(Song.objects.filter(pk=self.song.id))
