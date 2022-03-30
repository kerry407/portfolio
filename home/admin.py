from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = [ 'id','name', 'about_img', 'about_text'] 

@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):

    list_display = ['name', 'img_src']

@admin.register(Work)
class Works(admin.ModelAdmin):
    
    list_display = ['title', 'description' ,'work_image']
    
@admin.register(Contact)
class Works(admin.ModelAdmin):
    
    list_display = ['fullname', 'email' ,'message']