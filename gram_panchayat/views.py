from django.shortcuts import render, redirect
from .models import Celebrity, Event, Gallery, GramSabhaMeeting,Infrastructure,Development, Sarpanch, Scheme,staffs,members,Document
from .forms import complain_form, contact_form
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.utils import timezone


# Create your views here.

class AppLoginView(LoginView):
    template_name = "registration/login.html"
    def form_valid(self, form):
        remember = self.request.POST.get("remember_me")
        return super().form_valid(form)
    

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
    images = Gallery.objects.all().order_by('-created_at') 
    return render(request, "gallery.html",{'images':images})

def sarpanch(request):
    sarpanch_detail = Sarpanch.objects.all()
    srp_detail = []
    for item in sarpanch_detail:
        points = []
        if item.extra_points:
            points = [p.strip() for p in item.extra_points.split('\n')]
        srp_detail.append({
            'detail': item,
            'points': points
        })
    return render(request, 'sarpanch.html', {'sarpanch_list': srp_detail})

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
        staff_members = staffs.objects.all().order_by('staff_mem_name')
        return render(request, "staff_member.html", {
            "title": "OUR PANCHAYAT STAFF",
            "person": staff_members
        })
    elif page_type == "member":
        member_list = members.objects.all().order_by('member_name')
        return render(request, "staff_member.html", {
            "title": "OUR PANCHAYAT MEMBERS",
            "person": member_list
        })
    else:
        return render(request, "staff_member.html", {
            "title": "Not Found",
            "person": []
        })


def history(request):
    return render(request,'history.html')

def devlopment(request):
    devlopments = Development.objects.all().order_by('year')
    return render(request,'devlopment.html',{'developments':devlopments})

def celebrity(request):
    celebritys = Celebrity.objects.all().order_by('-created_at')
    return render(request,'celebrity.html',{'celebritys':celebritys})

def gramsabha(request):
    today = timezone.now().date()
    upcoming_meetings = GramSabhaMeeting.objects.filter(date__gte=today).order_by('date')
    past_meetings = GramSabhaMeeting.objects.filter(date__lt=today).order_by('-date')

    return render(request, "gramsabha.html", {
        "upcoming_meetings": upcoming_meetings,
        "past_meetings": past_meetings
    })

def celebrity_detail(request,celebrity_id):
    celebrity = get_object_or_404(Celebrity,id=celebrity_id)
    # print(celebritys)
    # Split extra_points by comma into a list
    points = []
    if celebrity.extra_points:
        points = [p.strip() for p in celebrity.extra_points.split('\n')]
    
    return render(request, 'celebrity_detail.html', {'celebrity': celebrity, 'points': points})

def scheme(request):
    schemes = Scheme.objects.all().order_by('-created_at')
    return render(request,'scheme.html',{'schemes':schemes})

def download(request):
    documents = Document.objects.all()  # Users can see list
    return render(request, 'download.html', {'documents': documents})

def infrastructure(request):
    infra = Infrastructure.objects.all().order_by('created_at')

    infra_with_points = []
    for item in infra:
        points = []
        if item.extra_points:
            points = [p.strip() for p in item.extra_points.split('\n')]
        infra_with_points.append({
            'object': item,
            'points': points
        })
    return render(request, 'Infrastructure.html', {'infra_with_points': infra_with_points})


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


