from django.shortcuts import render,redirect

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

