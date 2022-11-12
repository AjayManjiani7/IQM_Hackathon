from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'janta/login.html')

def register(request):
    return render(request, 'janta/register.html')