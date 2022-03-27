from django.contrib import admin

# Register your models here.
from .models import Image,Category,Location,category

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)

