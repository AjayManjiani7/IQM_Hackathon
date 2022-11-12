from django.shortcuts import render
from .models import Department, Department_user
# Create your views here.

def login(request):
    return render(request, 'department/login.html')

def dashboard(request , dept):

    Dept_usr = Department_user.objects.filter(user=request.user , department__name__contains = dept)

    return render(request, 'department/dashboard.html')