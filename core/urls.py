from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services, name="services"),
    path('service-details/<slug:service_slug>/', views.service_details, name="service_details"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('contactus/', views.contactus, name="contactus"),
    
]
