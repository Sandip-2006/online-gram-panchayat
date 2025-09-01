from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="home"),
    path('complain/',views.complain,name="compalin"),
    path('contact/',views.contact,name="contact"),
    path('gallery/',views.gallery,name="gallery"),
]
