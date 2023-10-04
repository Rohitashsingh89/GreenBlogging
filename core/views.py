from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect

from .models import FeatureService, Services, Skill, Testimonials, WidgetItem
from blog.models import BlogPost
from .forms import ContactForm, HomeContactForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

def home(request):
    services = Services.objects.all()
    latest_blog_posts = BlogPost.objects.order_by('-publish_date')[:3]
    testimonials = Testimonials.objects.all()
    skills = Skill.objects.all()
    feature_services = FeatureService.objects.all()
    widget_items = WidgetItem.objects.all()

    context ={
        'services': services,
        'latest_blog_posts': latest_blog_posts,
        'testimonials': testimonials,
        'skills': skills,
        'feature_services': feature_services,
        'widget_items': widget_items
    }
    return render(request, 'index.html', context=context)

def about(request):
    feature_services = FeatureService.objects.all()

    return render(request, 'about.html', {'feature_services': feature_services })

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', {'services': services})

def service_details(request, service_slug):
    if not request.session.get(f'viewed_{service_slug}'):  
        try:
            service_detail = get_object_or_404(Services, slug=service_slug)
           
            request.session[f'viewed_{service_slug}'] = True
        except Services.DoesNotExist:
            raise Http404("Blog post does not exist")
    else:
        # If the post has already been viewed in this session, retrieve it without incrementing views
        service_detail = get_object_or_404(Services, slug=service_slug)
    try:
        author_profile = service_detail.author.userprofile  
    except ObjectDoesNotExist:
        author_profile = None

    service_categories = service_detail.categories
    service_tags = service_detail.tags
    recent_posts = Services.objects.order_by('-created_at')[:3]
    recommended_posts = BlogPost.objects.order_by('-publish_date')[:3]

    context = {
        'service_detail': service_detail, 
        'service_categories': service_categories, 
        'service_tags': service_tags,
        'author_profile': author_profile,
        'recent_posts': recent_posts,
        'recommended_posts': recommended_posts
    }

    return render(request, 'service_details.html', context=context)

def contact(request):
    if request.method == 'POST':
        form = HomeContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Sending an email
            subject = f'Contact Form Submission by {contact.email}'
            message = f'Name: {contact.phone}\nEmail: {contact.email}\nMessage: {contact.message}'
            from_email = 'rohitashsinghcs20@bsacet.org'  
            recipient_list = {contact.email}
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            messages.success(request, 'Your message was sent successfully!!') 
            return redirect('contactus')
                 
        else: 
            messages.error(request, 'An error occurred while contacting!!') 

    else:
        form = HomeContactForm()
    return render(request, 'index.html', {'form': form})

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Sending an email
            subject = f'Contact Form Submission by {contact.email}'
            message = f'Name: {contact.first_name}\nEmail: {contact.email}\nMessage: {contact.message}'
            from_email = 'rohitashsinghcs20@bsacet.org'  
            recipient_list = [contact.email]
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            messages.success(request, 'Your message was sent successfully!!') 
            return redirect('contactus')
        else:
            messages.error(request, 'An error occurred while contacting!!') 

    else:
        form = ContactForm()
    return render(request, 'contactus.html', {'form': form})
