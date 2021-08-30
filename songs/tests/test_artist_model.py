from faker import Faker
from rest_framework.test import APITestCase

from ..models import Artist

fake = Faker()


class ArtistModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.artist = Artist.objects.create(name=fake.first_name())

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.artist.name, str)

    def test_str_models_methods(self):
        self.assertEquals(f"<Artists: {self.artist.name}>", str(self.artist))
