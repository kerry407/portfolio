from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import ContactForm



# Create your views here.

def home(request):
    about = About.objects.all()
    tech = Tech.objects.all()
    proj_1 = Work.objects.get(pk=1)
    proj_2 = Work.objects.get(pk=2)

    # form handle logic

    if request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
            name = contactform.cleaned_data.get('name')
            email = contactform.cleaned_data.get('email')
            messages.success(request, 'Message successfuly sent!')
            return redirect('home')
        else:
            messages.error(request, 'Error while making request')
    else:
        contactform = ContactForm()


    context = {
        'about': about,
        'tech': tech,
        'proj_1': proj_1,
        'proj_2': proj_2,
        'contactform': contactform
    }
    return render(request, 'portfolio/index.html', context)
    