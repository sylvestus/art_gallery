from django.http import HttpResponse, Http404
from email import message
from unicodedata import category
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from urllib import request
from.models import Image, Category, Location


# Create your views here.
def gen_landing(request):
    message = "landing page"
    highlight = Image.highlights()
    return render(request, 'generalpics.html', {'message': message, 'highlight': highlight})


def pic_per_location(request):
    if 'location' in request.GET and request.GET["location"]:
        location = request.GET.get('location')
        pic_per_location=Image.get_by_location(location)
        message = f"{location}"
        return render(request,"picperlocation.html", {"pic_per_location":pic_per_location,'message':message})
    else:
        message = "You haven't searched for any images taken in any location"
        return render(request, 'picperlocation.html', {"message": message})

def single_pic_details(request, id):
    message = 'picture details go here'
    single_pic = Image.get_image_by_id(id=id)
    return render(request, 'singlepicdetail.html', {'message': message, 'single_pic': single_pic})


def searched(request):
    print(request)
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'searched.html',{"message":message,"searched_articles":searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searched.html',{"message":message})

     


