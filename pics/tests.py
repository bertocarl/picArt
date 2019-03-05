from django.test import TestCase
from .models import Location,Category,Image


class LocationTestclass(TestCase):
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class ImageTestclass(TestCase):
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

class CategoryTestclass(TestCase):
    def test_save_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)