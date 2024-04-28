

from django.shortcuts import render
from django.contrib import messages
# about_view,services_view,blog_view
def home_view(request):
    return render(request, "index.html" )

def about_view(request):
    return render(request, "about.html" )

def about2_view(request):
    return render(request, "about-2.html" )

def gallery_view(request):
    return render(request, "gallery.html" )

def contact_view(request):
    return render(request, "contact.html" )

def homepage2_view(request):
    return render(request, "homepage-2.html" )

def homepage3_view(request):
    return render(request, "homepage-3.html" )