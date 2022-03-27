from email.mime import image
from unicodedata import name
from django.test import TestCase
from .models import Image,Category,Location


# Create your tests here.
class ImageTestClass(TestCase):
    # setup method
    def setUp(self):
        self.bikes=Image(image_name='bikes',image='',description='hello beautiful')
        self.bikes.save_image()
        
        self.new_location=Location(name='Baringo')
        self.new_location.save_location()

        self.new_category = Category(name='Travels')
        self.new_category.save_category()

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.bikes,Image))

     # tesing save method
    def test_save_method(self):
        # self.bikes.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

     # tesing delete method
    def test_delete_method(self):
        self.bikes.filter(id = 1).delete_image()
        images= Image.objects.all()
        self.assertTrue(len(images)<1)

    def test_update_method(self):
        # self.bikes.save_image()
        self.bikes.update_image()
        images = Image.objects.filter(id = 1).update(image_name ='Kim')

        self.assertTrue(images.image_name!= 'bikes')


    


