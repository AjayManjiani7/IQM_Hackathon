from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'department/login.html')

def dashboard(request):
    return render(request, 'department/dashboard.html')