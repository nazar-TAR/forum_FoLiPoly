
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def help(request):
    return render(request, 'main/help.html')

def signup(request):
    return render(request, 'main/signup.html')

def contact(request):
    return render(request, 'main/contact.html')