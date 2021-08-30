import songs
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Artist
from ..serializers import ArtistSerializer
from ..views import SongView

fake = Faker()


class ArtistModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artist = Artist.objects.create(name=fake.first_name())

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.artist.name, str)

    def test_str_models_methods(self):
        self.assertEquals(f"<Artists: {self.artist.name}>", str(self.artist))
