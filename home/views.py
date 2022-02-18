from datetime import datetime
from django.shortcuts import render, HttpResponse

from home.models import Contact

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email=email, desc=desc, date= datetime.today())
        contact.save()
    return render(request, 'contact.html')


def tour(request):
    return render(request, 'tour.html')

def map(request):
    return render(request, 'map.html')

def gallery(request):
    return render(request, 'gallery.html')
    
      
# Create your views here.
