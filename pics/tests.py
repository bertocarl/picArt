from django.test import TestCase
from .models import Location,Category,Image


# class CategoryTestClass(TestCase):
#  # Set up method
#     def setUp(self):
#         self.type= Category(name ='sports')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.type,Category))

#     def test_init(self):
       
#         self.assertTrue(self.type.name == 'sports')

#     def test_save_method(self):
#         self.type.save_category()
#         categories = Category.objects.all()
#         self.assertTrue(len(categorys)> 0)
    
#     def test_delete_method(self):
#         self.type.save_category()
#         categories = Category.objects.all()
#         self.type.delete_category()
#         categories = Category.objects.all()
#         self.assertTrue(len(categories)==0)

    

class LocationTestClass(TestCase):
    def setUp(self):
        self.place= Location(name ='Rwanda')

    def test_instance(self):
        self.assertTrue(isinstance(self.place,Location))

    def test_init(self):
        self.assertTrue(self.place.name =='Rwanda')

    def test_save_method(self):
        self.place.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)> 0)

    # def test_delete_method(self):
    #     self.place.save_location()
    #     locations = Location.objects.all()
    #     self.place.delete_location()
    #     locations = Location.objects.all()
    #     self.assertTrue(len(locations)==0)

class ImageTestCase(TestCase):
    def setUp(self):
        """
        This will create a new image before each test case
        """
        sports = Category(name = "sports")
        sports.save()
        Rwanda = Location(name = "Rwanda")
        Rwanda.save()
        self.new_image = Image(name = "image",description = "rollball world cup",location = 'Rwanda',category = 'sports')
    
    def defaultTestResult(self):
        """
        This will clear the db after each test
        """
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
    

    # def test_instance(self):
       
    #     self.assertTrue(isinstance(self.new_image, Image))
    
    def test_save_image(self):
       
        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)
    
    # def test_filter_by_location(self):
        
    #     self.new_image.save_image()
    #     self.assertTrue(len(Image.filter_by_location("Rwanda")) >0)

    # def test_delete_method(self):
    #     self.new_image.save_image()
    #     images = Image.objects.all()
    #     self.new_image.delete_image()
    #     images = Image.objects.all()
    #     self.assertTrue(len(images)==0)
    
    # def test_search_by_category(self):

    #     self.new_image.save_image()
    #     self.assertTrue(len(Image.search_by_category("sports"))>0)