from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="home"),
<<<<<<< HEAD
    path('complain/',views.complain,name="compalin"),
=======
    path('contact/',views.contact,name="contact"),
>>>>>>> 8c99a8b01db18f604c74ea6a6a0389a1742ace03
]
