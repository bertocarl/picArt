from django.test import TestCase
from .models import Location,Category,Image


class LocationTestclass(TestCase):
    def test_save_method(self):
        self.rwanda.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

