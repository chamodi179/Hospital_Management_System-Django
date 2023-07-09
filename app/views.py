from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import HMS_User

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

def signup(request):
    if request.method == 'POST':
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        address = request.POST['address']
        email = request.POST['email']
        contact = request.POST['contact']
        age = request.POST['age']
        password = request.POST['password']

        user = HMS_User(last_name=last_name, first_name=first_name, address=address, email=email, contact=contact, age=age, password=password)
        user.save()

        return redirect('index')  # Redirect to a success page or another URL
        # return render(request, 'index.html')

    return render(request, 'index.html')