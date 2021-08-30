from faker import Faker
from rest_framework.test import APITestCase

from ..models import Artist, Song

fake = Faker()


class SongModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artist = Artist.objects.create()
        cls.song = Song.objects.create(
            title=fake.first_name(), artist=cls.artist, votes=fake.random_digit()
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.song.title, str)
        self.assertIsInstance(self.song.artist, object)
        self.assertIsInstance(self.song.votes, int)

    def test_str_models_methods(self):
        self.assertEquals(f"<Songs: {self.song.title}>", str(self.song))

    def test_it_can_be_attached_to_multiple_artists(self):
        artist = Artist.objects.create(name=fake.first_name())

        songs = [
            Song.objects.create(
                title=fake.first_name(), artist=artist, votes=fake.random_digit()
            )
            for _ in range(3)
        ]

        for song in songs:
            self.assertEquals(artist.id, song.artist.id)
