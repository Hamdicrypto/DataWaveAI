from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index, name='index'),
    path('contact-us-light/', views.contact_us_light, name='contact_us_light'),
    path('about-light/', views.about_light, name='about-light'),
    path('blog-light/', views.blog_light, name='blog-light'),
    path('services-light/', views.services_light, name='services-light'),
    path('price-light/', views.price_light, name='price-light'),
]
