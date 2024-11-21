from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Social, Doctors, Landing, AboutUs, Message, Slug, Departments,Comments
from django.contrib import messages




from .models import AboutUs, Social, Doctors, Landing, Departments, Slug, Comments

class IndexView(View):
    def get(self, request):
        # Fetch data from all relevant models
        socials = Social.objects.all()  # Fetch all social media links
        doctors = Doctors.objects.all()  # Fetch all doctors
        landings = Landing.objects.all()  # Fetch all landing page data
        about_us_entries = AboutUs.objects.first()  # Fetch a single AboutUs entry (assuming it's just one)
        departments = Departments.objects.all()  # Fetch all departments
        slides = Slug.objects.all()  # Fetch Slug data for the carousel
        comments = Comments.objects.all()  # Fetch all comments

        # Prepare context dictionary to pass data to the template
        context = {
            'socials': socials,
            'doctors': doctors,
            'landings': landings,
            'about_us_entries': about_us_entries,  # Single AboutUs entry
            'departments': departments,
            'slides': slides,
            'comments': comments,
        }

        # Render the index template with the provided context data
        return render(request, 'index.html', context)

# About Us View
def about_view(request):
    about_us = AboutUs.objects.all()
    return render(request, 'about.html', {'about_us': about_us})

# Doctors View
def doctors_view(request):
    doctors = Doctors.objects.all()  # Removed select_related('social_media')
    return render(request, 'doctors.html', {'doctors': doctors})

# Departments View
def departments_view(request):
    departments = Departments.objects.all()
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
