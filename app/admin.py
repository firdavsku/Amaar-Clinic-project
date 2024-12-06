from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class MultilingualAdminMixin(admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        model = self.model
        multilingual_fields = [field.name for field in model._meta.fields if any(lang in field.name for lang in ["_en", "_ru", "_kk"])]
        general_fields = [field.name for field in model._meta.fields if field.name not in multilingual_fields]
        multilingual_fieldsets = [
            (lang.upper(), {"fields": [f for f in multilingual_fields if f.endswith(f"_{lang}")], "classes": ["collapse"]})
            for lang in ["en", "ru", "kk"]
        ]
        return [
            (None, {"fields": general_fields}),
            *multilingual_fieldsets,
        ]

from .models import (
    Social, Slug, Service, Gallery, Doctor, Landing, 
    AboutUs, Message, Comment, Department
)


# Social Admin
@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


# Slug Admin
@admin.register(Slug)
class SlugAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("English"), {"fields": ("title_en", "content_en")}),
        (_("Russian"), {"fields": ("title_ru", "content_ru")}),
        (_("Kazakh"), {"fields": ("title_kk", "content_kk")}),
    )
    list_display = ("title_en", "title_ru", "title_kk")
    search_fields = ("title_en", "title_ru", "title_kk")



# Service Admin
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Profile"), {"fields": ("service_image",)}),
        (_("English"), {"fields": ("service_name_en", "service_description_en")}),
        (_("Russian"), {"fields": ("service_name_ru", "service_description_ru")}),
        (_("Kazakh"), {"fields": ("service_name_kk", "service_description_kk")}),
    )
    list_display = ("service_name_en", "service_name_ru", "service_name_kk")
    search_fields = ("service_name_en", "service_name_ru", "service_name_kk")



# Doctor Admin
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Profile"), {
            "fields": ("profile_image", "contact_number", "email_address"),
        }),
        (_("English"), {
            "fields": ("full_name_en", "job_title_en"),
        }),
        (_("Russian"), {
            "fields": ("full_name_ru", "job_title_ru"),
        }),
        (_("Kazakh"), {
            "fields": ("full_name_kk", "job_title_kk"),
        }),
    )

# Landing Admin
@admin.register(Landing)
class LandingAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("English"), {"fields": ("headline_en", "description_en")}),
        (_("Russian"), {"fields": ("headline_ru", "description_ru")}),
        (_("Kazakh"), {"fields": ("headline_kk", "description_kk")}),
    )
    list_display = ("headline_en", "headline_ru", "headline_kk")
    search_fields = ("headline_en", "headline_ru", "headline_kk")


# AboutUs Admin
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Profile"), {"fields": ("image", "video_file", "contact_number")}),
        (_("English"), {"fields": ("headline_en", "name_en", "address_en")}),
        (_("Russian"), {"fields": ("headline_ru", "name_ru", "address_ru")}),
        (_("Kazakh"), {"fields": ("headline_kk", "name_kk", "address_kk")}),
        (_("Social Media"), {"fields": ("social_media",)}),
    )
    list_display = ("headline_en", "name_en", "contact_number")
    search_fields = ("headline_en", "name_en", "name_ru", "name_kk")


# Message Admin
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender_name', 'contact_number')  # Update fields to 'sender_name' and 'contact_number'
    search_fields = ('sender_name', 'contact_number')


# Comment Admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'commenter_name', 'comment_text')  # Update fields to 'commenter_name' and 'comment_text'
    search_fields = ('commenter_name', 'comment_text')


# Department Admin
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Profile"), {"fields": ("banner_image",)}),
        (_("English"), {"fields": ("department_name_en", "description_en")}),
        (_("Russian"), {"fields": ("department_name_ru", "description_ru")}),
        (_("Kazakh"), {"fields": ("department_name_kk", "description_kk")}),
    )
    list_display = ("department_name_en", "department_name_ru", "department_name_kk")
    search_fields = ("department_name_en", "department_name_ru", "department_name_kk")





# Gallery Admin
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_file')  # Use 'image_file' instead of 'image'
    search_fields = ('image_file',)
