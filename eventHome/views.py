from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home.html")

def feedback(request):
    return render(request, "feedback.html")

def signup(request):
    return render(request, "signup.html")

def regtrip(request):
    return render(request, "regtrip.html")