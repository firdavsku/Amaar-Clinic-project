from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Social, Doctors, Landing, AboutUs, Message, Comments, Departments

class IndexView(View):
    def get(self, request):
        # Fetch data from all relevant models
        socials = Social.objects.all()
        doctors = Doctors.objects.all()
        landings = Landing.objects.all()
        about_us_entries = AboutUs.objects.all()
        departments = Departments.objects.all()

        # Pass all data to the template
        context = {
            'socials': socials,
            'doctors': doctors,
            'landings': landings,
            'about_us_entries': about_us_entries,
            'departments': departments,
        }
        
        return render(request, 'index.html', context)