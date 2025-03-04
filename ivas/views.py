from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "html/index.html")  # This looks for index.html in templates folder

def galerija(request):
    return render(request, "html/gallery.html")

def photos(request):
    return render(request, "html/photos.html")

def contact(request):
    return render(request, "html/contact.html")

def about_us(request):
    return render(request, "html/about.html")
