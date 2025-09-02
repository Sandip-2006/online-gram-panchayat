from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def complain(request):
    return render(request, "complain.html")

def gallery(request):
    return render(request, "gallery.html")

def sarpanch(request):
    return render(request, "sarpanch.html")

def event(request):
    return render(request, "event.html")

def contact(request):
    return render(request, "contact.html")
