from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="home"),
    path('complain/',views.complain,name="complain"),
    path('contact/',views.contact,name="contact"),
    path('gallery/',views.gallery,name="gallery"),
    path('sarpanch/',views.sarpanch,name="sarpanch"),
    path('event/',views.event,name="event"),
    path('history/',views.history,name="history"),
    path('devlopment/',views.devlopment,name="development"),
    path('<str:page_type>/',views.staff_member,name="staff_member"),
]
