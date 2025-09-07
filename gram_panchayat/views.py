from django.shortcuts import render, redirect
from .models import Celebrity, Event
from .forms import complain_form, contact_form
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "index.html")

def complain_create(request):
    if request.method == 'POST':
        form = complain_form(request.POST, request.FILES)
        if form.is_valid():
            complains = form.save(commit=False)
            complains.save()
            messages.success(request, "Complaint submitted successfully!")
            return redirect('home')
    else:
        form = complain_form()
    return render(request, "complain.html", {'form': form})


def about(request):
    return render(request, "about.html")

def gallery(request):
    return render(request, "gallery.html")

def sarpanch(request):
    return render(request, "sarpanch.html")

def event(request):
    events = Event.objects.all().order_by("-date")
    return render(request, "event.html",{'events':events})

def contact(request):
    if request.method == "POST":
        form = contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message has been send successfully!')
            return redirect('contact')
        # else:
        #     messages.error(request,'Please correct the errors below.')
    else:
            form = contact_form()

    return render(request, "contact.html", {'form': form})

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
    celebritys = Celebrity.objects.all().order_by('-created_at')
    return render(request,'celebrity.html',{'celebritys':celebritys})

def gramsabha(request):
    return render(request,'gramsabha.html')

def celebrity_detail(request,celebrity_id):
    celebrity = get_object_or_404(Celebrity,id=celebrity_id)
    # print(celebritys)
    # Split extra_points by comma into a list
    points = []
    if celebrity.extra_points:
        points = [p.strip() for p in celebrity.extra_points.split(',')]
    
    return render(request, 'celebrity_detail.html', {'celebrity': celebrity, 'points': points})

def scheme(request):
    return render(request,'scheme.html')

def download(request):
    return render(request,'download.html')

def Infrastructure(request):
    return render(request,'Infrastructure.html')

# dont touch this file its for robots.txt
from django.http import HttpResponse

# def robots_txt(request):
#     content = """
#     User-agent: *
#     Disallow: /admin/
#     Disallow: /static/
#     Disallow: /media/
#     Disallow: /__reload__/
#     Disallow: /accounts/
#     Disallow: /complain/
#     Disallow: /staff/

#     Sitemap: https://yourdomain.com/sitemap.xml
#     """
#     return HttpResponse(content, content_type="text/plain")
