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

def staff_member(request, page_type):
    if page_type == "staff":
        context={"title": "OUR PANCHAYAT STAFF", "person": [
            {"name": "Suthar Gunvant lal", "position": "Sarpanch", "contact": "1234567890", "image": "images/member.png"},
            {"name": "Jane Smith", "position": "Panchayat Member", "contact": "0987654321", "image": "images/download.jpg"},
        ]}
    elif page_type == "member":
        context={"title": "OUR PANCHAYAT MEMBERS", "person": [
            {"name": "Alice Brown", "position": "Member", "contact": "1122334455", "image": "images/images.jpg"},
            {"name": "Bob White", "position": "Member", "contact": "2233445566", "image": "images/panch.jpg"},
        ]}
    else:
        context = {"title": "home", "description": "Welcome to the Panchayat"}
    return render(request, "staff_member.html", context)
        