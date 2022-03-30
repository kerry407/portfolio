from django.db import models
# Create your models here.

    
class About(models.Model):

    name = models.CharField(max_length=40, null=True, blank=True)
    about_img = models.ImageField(upload_to='uploads', height_field=None, width_field=None)
    about_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Tech(models.Model):
    
    name = models.CharField(max_length=50, null=True, blank=True)
    img_src = models.CharField(max_length=400)

    def __str__(self):
        return self.name
    

class Work(models.Model):
    
    title = models.CharField(max_length=70)
    description = models.TextField(default = 'description')
    work_image = models.ImageField(upload_to='uploads')
    
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    
    fullname = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    
        
