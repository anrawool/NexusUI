from django.shortcuts import render
# Create your views here.

def Home(request):
    return render(request, 'index.html')

def Passwords(request):
    return render(request, 'password.html')