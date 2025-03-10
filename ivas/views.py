from django.shortcuts import render

from .models import Slika


# Create your views here.
def home(request):
    return render(request, "html/index.html")  # This looks for index.html in templates folder

def galerija(request):

    slike = Slika.objects.all()

    context = {"slike": slike}

    return render(request,"html/gallery.html",context)

def photos(request):
    return render(request, "html/photos.html")

def contact(request):
    return render(request, "html/contact.html")

def about_us(request):
    return render(request, "html/about.html")
