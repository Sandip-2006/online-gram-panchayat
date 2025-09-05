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
            {"name": "Suthar Gunvant lal", "position": "Sarpanch", "contact": "1234567890", "image": "images/member.png"},
            {"name": "Jane Smith", "position": "Panchayat Member", "contact": "0987654321", "image": "images/download.jpg"},
            {"name": "Suthar Gunvant lal", "position": "Sarpanch", "contact": "1234567890", "image": "images/member.png"},
            {"name": "Jane Smith", "position": "Panchayat Member", "contact": "0987654321", "image": "images/download.jpg"},
            {"name": "Suthar Gunvant lal", "position": "Sarpanch", "contact": "1234567890", "image": "images/member.png"},
            {"name": "Jane Smith", "position": "Panchayat Member", "contact": "0987654321", "image": "images/download.jpg"},
            {"name": "Suthar Gunvant lal", "position": "Sarpanch", "contact": "1234567890", "image": "images/member.png"},
            {"name": "Jane Smith", "position": "Panchayat Member", "contact": "0987654321", "image": "images/download.jpg"},
            {"name": "Suthar Gunvant lal", "position": "Sarpanch", "contact": "1234567890", "image": "images/member.png"},
        ]}
           
    elif page_type == "member":
        context={"title": "OUR PANCHAYAT MEMBERS", "person": [
            {"name": "Alice Brown", "position": "Member", "contact": "1122334455", "image": "images/images.jpg"},
            {"name": "Bob White", "position": "Member", "contact": "2233445566", "image": "images/panch.jpg"},
        ]}
    else:
        context = {"title": "404 NOT FOUND :)", "description": "Welcome to the Panchayat"}
    return render(request, "staff_member.html", context)


def history(request):
    return render(request,'history.html')

def devlopment(request):
    return render(request,'devlopment.html')

def celebrity(request):
    return render(request,'celebrity.html')

def gramsabha(request):
    return render(request,'gramsabha.html')

def celebrity_detail(request):
    return render(request,'celebrity_detail.html')

def scheme(request):
    return render(request,'scheme.html')

def download(request):
    return render(request,'download.html')

def Infrastructure(request):
    return render(request,'Infrastructure.html')

# dont touch this file its for robots.txt
from django.http import HttpResponse

def robots_txt(request):
    content = """
    User-agent: *
    Disallow: /admin/
    Disallow: /static/
    Disallow: /media/
    Disallow: /__reload__/
    Disallow: /accounts/
    Disallow: /complain/
    Disallow: /staff/

    Sitemap: https://yourdomain.com/sitemap.xml
    """
    return HttpResponse(content, content_type="text/plain")
