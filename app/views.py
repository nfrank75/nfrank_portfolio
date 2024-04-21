from django.shortcuts import render
from .models import Contact, Service, Job, Education, Project, CV


def home(request):
    return render(request, 'app/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
            
        # ...envoi d'un e-mail de notification

        # Redirigez l'utilisateur vers une page de succès ou affichez un message de succès
        # return render(request, 'success.html')
        # else:
        #     form = ContactForm()

    return render(request, 'app/contact.html')

def about(request):
    return render(request, 'app/about.html')

def blog(request):
    return render(request, 'app/blog.html')

def service(request):
    services = Service.objects.all().order_by('-updated_at')
    return render(request, 'app/service.html', {'services': services}) 


def project(request):
    projects = Project.objects.all().order_by('-updated_at')
    return render(request, 'app/project.html', {'projects': projects})

 
def job(request):
    jobs = Job.objects.all().order_by('-updated_at')
    return render(request, 'app/job.html', {'jobs': jobs})

 
def education(request):
    educations = Education.objects.all().order_by('-updated_at')
    return render(request, 'app/education.html', {'educations': educations})

def cv(request):
    cv = CV.objects.all().order_by('-updated_at')
    return render(request, 'app/cv.html', {'cv': cv})

 

