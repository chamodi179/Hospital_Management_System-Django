from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'index.html', {'navbar': 'index'})

def user_signup(request):
    return render(request, "user_signup.html")

def About(request):
    return render(request, "About.html", {'navbar': 'About'})

def Contact(request):
    return render(request, "Contact.html", {'navbar': 'Contact'})

def Services(request):
    return render(request, "Services.html", {'navbar': 'Services'})

def cosmetic_view(request):
    return render(request, 'services_template.html', {'selected_center': 'cosmetic'})

def BC_CENTRE_view(request):
    return render(request, 'services_template.html', {'selected_center': 'BC_CENTRE'})

def GASTROENTEROLOGY_view(request):
    return render(request, 'services_template.html', {'selected_center': 'GASTROENTEROLOGY'})

def HEALTH_CHECK_view(request):
    return render(request, 'services_template.html', {'selected_center': 'HEALTH_CHECK'})

def KIDNE_CARE_C_view(request):
    return render(request, 'services_template.html', {'selected_center': 'KIDNE_CARE_C'})

def FERTILITY_CENTRE_view(request):
    return render(request, 'services_template.html', {'selected_center': 'FERTILITY_CENTRE'})

def HEART_CENTRE_view(request):
    return render(request, 'services_template.html', {'selected_center': 'HEART_CENTRE'})

def W_WELLNESS_view(request):
    return render(request, 'services_template.html', {'selected_center': 'W_WELLNESS'})

def UROLOGY_CARE_C_view(request):
    return render(request, 'services_template.html', {'selected_center': 'UROLOGY_CARE_C'})

def MENS_WELLNESS_C_view(request):
    return render(request, 'services_template.html', {'selected_center': 'MENS_WELLNESS_C'})

def go_back(request):
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url is None:
        return redirect('index')
    else:
        return redirect(previous_url)

