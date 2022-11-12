from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'janta/login.html')

def register(request):
    return render(request, 'janta/register.html')


def Complaint(request):
    return render(request, 'janta/complaint.html')

def dashboard(request):
    return render(request, 'janta/dashboard.html')

def status(request):
    return render(request, 'janta/status.html')