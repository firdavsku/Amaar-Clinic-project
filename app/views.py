from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Social, Doctor, Landing, AboutUs, Message, Slug, Department,Comment,Service,Gallery
from django.contrib import messages
from config import settings
from django.utils.translation import activate
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import django
from django.utils import translation



class IndexView(View):
    def get(self, request):
        socials = Social.objects.all() 
        doctors = Doctor.objects.all()  
        landings = Landing.objects.all()  
        about_us_entries = AboutUs.objects.first()
        departments = Department.objects.all()
        slides = Slug.objects.all()  
        comments = Comment.objects.all()  
        services = Service.objects.all()
        gallery = Gallery.objects.all()
        context = {
            'socials': socials,
            'doctors': doctors,
            'landings': landings,
            'about_us': about_us_entries,  
            'departments': departments,
            'slides': slides,
            'comments': comments,
            'services':services,
            'gallery':gallery,
        }
        return render(request, 'index.html', context)


class ServicesListView(View):
    def get(self, request):
        services = Service.objects.all()
        return render(request, 'services.html', {'services': services})
    

# About Us View
def about_view(request):
    about_us = AboutUs.objects.all()
    return render(request, 'about.html', {'about_us': about_us})

# Doctors View
def doctors_view(request):
    doctors = Doctor.objects.all()  # Removed select_related('social_media')
    return render(request, 'doctors.html', {'doctors': doctors})

# Departments View
def departments_view(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def contact_view(request):
    if request.method == 'POST':
        # Get the data from the form
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the data to the Message model
        Message.objects.create(
            full_name=full_name,
            phone=phone,
            message=message
        )

        # Add a success message
        messages.success(request, 'Your message has been sent successfully!')

    return render(request, 'contact.html')

def switch_language(request):
    language = request.GET.get('language', 'en')
    next_url = request.GET.get('next', '/')
    activate(language)
    response = redirect(next_url)
    response.set_cookie('django_language', language)
    return response

