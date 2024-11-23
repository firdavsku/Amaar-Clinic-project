from django.db import models

# Create your models here.
class Social(models.Model):
    name=models.CharField(max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Social Network"
        verbose_name_plural = "Social Networks"
    

class Slug(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Slug"
        verbose_name_plural = "Slugs"
    
class Doctors(models.Model):
    image=models.ImageField(upload_to="images")
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

class Landing(models.Model):
    text = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.text
    class Meta:
        verbose_name = "Landing"
        verbose_name_plural = "Landings"

class AboutUs(models.Model):
    text = models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")
    name=models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    social_media = models.ForeignKey(Social, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=14)
    def __str__(self):
        return self.text
    class Meta:
        verbose_name = "About us"
        verbose_name_plural = "About us"


class Message(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

class Comments(models.Model):
    image = models.ImageField(upload_to='images')
    full_name = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    
    

class Departments(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
    