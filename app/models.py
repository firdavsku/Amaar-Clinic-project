from django.db import models
from django.utils.translation import gettext_lazy as _


class Social(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Social Network Name"))
    link = models.URLField(verbose_name=_("Profile URL"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Social Network")
        verbose_name_plural = _("Social Networks")


class Slug(models.Model):
    title_en = models.CharField(max_length=200, verbose_name=_("Slug Title (EN)"))
    title_ru = models.CharField(max_length=200, verbose_name=_("Slug Title (RU)"))
    title_kk = models.CharField(max_length=200, verbose_name=_("Slug Title (KK)"))
    content_en = models.TextField(verbose_name=_("Slug Content (EN)"))
    content_ru = models.TextField(verbose_name=_("Slug Content (RU)"))
    content_kk = models.TextField(verbose_name=_("Slug Content (KK)"))

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = _("Slug")
        verbose_name_plural = _("Slugs")


class Doctor(models.Model):
    profile_image = models.ImageField(upload_to="images", verbose_name=_("Profile Image"))
    full_name_en = models.CharField(max_length=50, verbose_name=_("Full Name (EN)"))
    full_name_ru = models.CharField(max_length=50, verbose_name=_("Full Name (RU)"))
    full_name_kk = models.CharField(max_length=50, verbose_name=_("Full Name (KK)"))
    job_title_en = models.CharField(max_length=50, verbose_name=_("Position (EN)"))
    job_title_ru = models.CharField(max_length=50, verbose_name=_("Position (RU)"))
    job_title_kk = models.CharField(max_length=50, verbose_name=_("Position (KK)"))
    contact_number = models.CharField(max_length=13, verbose_name=_("Phone Number"))
    email_address = models.EmailField(max_length=200, verbose_name=_("Email Address"))

    def __str__(self):
        return self.full_name_en

    class Meta:
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")


class AboutUs(models.Model):
    headline_en = models.TextField(null=True, blank=True, verbose_name=_("Headline Text (EN)"))
    headline_ru = models.TextField(null=True, blank=True, verbose_name=_("Headline Text (RU)"))
    headline_kk = models.TextField(null=True, blank=True, verbose_name=_("Headline Text (KK)"))
    image = models.ImageField(upload_to="images", verbose_name=_("Image"))
    name_en = models.CharField(max_length=50, verbose_name=_("Name (EN)"))
    name_ru = models.CharField(max_length=50, verbose_name=_("Name (RU)"))
    name_kk = models.CharField(max_length=50, verbose_name=_("Name (KK)"))
    address_en = models.CharField(max_length=200, verbose_name=_("Location (EN)"))
    address_ru = models.CharField(max_length=200, verbose_name=_("Location (RU)"))
    address_kk = models.CharField(max_length=200, verbose_name=_("Location (KK)"))
    social_media = models.ForeignKey(Social, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Social Media"))
    contact_number = models.CharField(max_length=14, verbose_name=_("Phone Number"))
    video_file = models.FileField(upload_to='videos', null=True, blank=True, verbose_name=_("Video File"))

    def __str__(self):
        return self.headline_en

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")


class Landing(models.Model):
    headline_en = models.CharField(max_length=100, verbose_name=_("Headline Text (EN)"))
    headline_ru = models.CharField(max_length=100, verbose_name=_("Headline Text (RU)"))
    headline_kk = models.CharField(max_length=100, verbose_name=_("Headline Text (KK)"))
    description_en = models.TextField(null=True, blank=True, verbose_name=_("Description (EN)"))
    description_ru = models.TextField(null=True, blank=True, verbose_name=_("Description (RU)"))
    description_kk = models.TextField(null=True, blank=True, verbose_name=_("Description (KK)"))

    def __str__(self):
        return self.headline_en

    class Meta:
        verbose_name = _("Landing Page")
        verbose_name_plural = _("Landing Pages")


class Message(models.Model):
    sender_name = models.CharField(max_length=100, verbose_name=_("Sender Full Name"))
    contact_number = models.CharField(max_length=100, verbose_name=_("Contact Number"))
    message_content = models.TextField(null=True, blank=True, verbose_name=_("Message Content"))

    def __str__(self):
        return self.sender_name

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")


class Comment(models.Model):
    profile_image = models.ImageField(upload_to='images', verbose_name=_("Profile Image"))
    commenter_name = models.CharField(max_length=100, verbose_name=_("Commenter Name"))
    comment_text = models.TextField(null=True, blank=True, verbose_name=_("Comment Text"))

    def __str__(self):
        return self.commenter_name

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class Department(models.Model):
    department_name_en = models.CharField(max_length=200, verbose_name=_("Department Name (EN)"))
    department_name_ru = models.CharField(max_length=200, verbose_name=_("Department Name (RU)"))
    department_name_kk = models.CharField(max_length=200, verbose_name=_("Department Name (KK)"))
    description_en = models.TextField(verbose_name=_("Department Description (EN)"), blank=True, null=True)
    description_ru = models.TextField(verbose_name=_("Department Description (RU)"), blank=True, null=True)
    description_kk = models.TextField(verbose_name=_("Department Description (KK)"), blank=True, null=True)
    banner_image = models.ImageField(upload_to='department_images/', verbose_name=_("Department Banner Image"))

    def __str__(self):
        return self.department_name_en

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


class Service(models.Model):
    service_image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name=_("Service Image"))
    service_name_en = models.CharField(max_length=200, verbose_name=_("Service Name (EN)"))
    service_name_ru = models.CharField(max_length=200, verbose_name=_("Service Name (RU)"))
    service_name_kk = models.CharField(max_length=200, verbose_name=_("Service Name (KK)"))
    service_description_en = models.TextField(null=True, blank=True, verbose_name=_("Service Description (EN)"))
    service_description_ru = models.TextField(null=True, blank=True, verbose_name=_("Service Description (RU)"))
    service_description_kk = models.TextField(null=True, blank=True, verbose_name=_("Service Description (KK)"))

    def __str__(self):
        return self.service_name_en

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")


class Gallery(models.Model):
    image_file = models.ImageField(upload_to='images', verbose_name=_("Image File"))

    def __str__(self):
        return f"Gallery Image {self.id}"

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Gallery")

