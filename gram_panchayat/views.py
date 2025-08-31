from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

<<<<<<< HEAD
def complain(request):
    return render(request,"complain.html")
=======
def contact(request):
    return render(request,"contact.html")
>>>>>>> 8c99a8b01db18f604c74ea6a6a0389a1742ace03
