from django.shortcuts import render
from pages.models import Team

# Create your views here.

def index(request):
    teams = Team.objects.all()
    data ={
        'teams': teams,
        
             }
    
    return render(request,'index.html',data)

def contact_us_light(request):
    return render(request, 'contact-us-light.html')

def about_light(request):
     teams = Team.objects.all()
     data ={
        
        'teams': teams,
        
              }
     
     return render(request, 'about-light.html',data)

def blog_light(request):
    return render(request, 'blog-light.html')

def services_light(request):
    return render(request, 'services-light.html')

def price_light(request):
    return render(request, 'price-light.html')
