from django.contrib import admin
from .models import Social, Doctors, Landing, AboutUs, Message, Comments, Departments,Slug

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):  # Renamed the admin class to SocialAdmin
    list_display = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Slug)

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'social_media')
    list_filter = ('social_media',)
    search_fields = ('name', 'position')
    autocomplete_fields = ('social_media',)

@admin.register(Landing)
class LandingAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'description')
    search_fields = ('text', 'description')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'name', 'location', 'social_media')
    list_filter = ('social_media',)
    search_fields = ('text', 'name', 'location')
    autocomplete_fields = ('social_media',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'message')
    search_fields = ('full_name', 'phone', 'message')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'message')
    search_fields = ('full_name', 'message')

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text')
    search_fields = ('name', 'text')
