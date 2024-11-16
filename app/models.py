from django.db import models

# Create your models here.
class Social(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Doctors(models.Model):
    image=models.ImageField(upload_to="images")
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    social_media=models.ForeignKey(Social, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Landing(models.Model):
    text = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.text

class AboutUs(models.Model):
    text = models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")
    name=models.CharField(max_length=50)
    location = models.URLField()
    social_media = models.ForeignKey(Social, on_delete=models.CASCADE)
    def __str__(self):
        return self.text


class Message(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)
    # is_comment = models.BooleanField(default=False)
    def __str__(self):
        return self.text

class Comments(models.Model):
    image = models.ImageField(upload_to='images')
    full_name = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.full_name
    

class Departments(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    