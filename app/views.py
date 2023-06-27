from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_signup(request):
    return render(request, "user_signup.html")

