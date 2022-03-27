from distutils.command.upload import upload
from email.policy import default
import re
from statistics import mode
from unicodedata import category
from django.db import models
import email
import datetime as dt


# Create your models here.

class Location(models.Model):
    location_name=models.CharField(max_length=50)

    def __str__(self):
        return self.location_name


    def save_location(self):
       self.save(self)
    @classmethod
    def list_locations(cls):
        locations=cls.objects.all()
        return locations

    @classmethod
    def update_location(cls,id):
        u_loc=cls.objects.filter(id=id).update()
        return u_loc
    @classmethod
    def delete_location(cls,id):
        d_loc=cls.objects.filter(id=id).update()
        return d_loc

class Category(models.Model):
    category_name=models.CharField(max_length=50)



    def __str__(self):
        return self.category_name


    def save_category(self):
       self.save(self)

    @classmethod
    def list_locations(cls):
        categories=cls.objects.all()
        return categories

    @classmethod
    def update_location(cls,id):
        u_cat=cls.objects.filter(id=id).update()
        return u_cat
    @classmethod
    def delete_location(cls,id):
        d_cat=cls.objects.filter(id=id).update()
        return d_cat

class Image(models.Model):
    image_name= models.CharField(max_length=50)
    image=models.ImageField(upload_to = 'articless/',default='')
    description=models.TextField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name
    
    def save_image(self):
       self.save(self)
    @classmethod
    def delete_image(cls,id):
        cls.objects.filter(id).delete()

    @classmethod
    def update_image(cls,id):
        cls.objects.filter(id).update() 

    @classmethod
    def highlights(cls):
        highlights= cls.objects.order_by('category')
        return highlights
    
    @classmethod
    def get_image_by_id(cls,id):
        image_per_id=cls.objects.filter(id = id).all()
        return image_per_id

    @classmethod
    def search_image(cls,search_term):
        image =cls.objects.filter(category__category_name__icontains=search_term)
        print(image)
        return image
    @classmethod
    def get_by_location(cls,location):
        image_per_location =cls.objects.filter(location__location_name__icontains= location)
        print(image_per_location)
        return image_per_location



    


    