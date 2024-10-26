from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact_us_light(request):
    return render(request, 'contact-us-light.html')

def about_light(request):
    return render(request, 'about-light.html')

def blog_light(request):
    return render(request, 'blog-light.html')

def services_light(request):
    return render(request, 'services-light.html')

def price_light(request):
    return render(request, 'price-light.html')
