from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def complain(request):
    return render(request, "complain.html")

def gallery(request):
    return render(request, "gallery.html")

def contact(request):
    return render(request, "contact.html")
