from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, '/portal/home.html')

def faq(request):
    return render(request, '/portal/faq.html')    
