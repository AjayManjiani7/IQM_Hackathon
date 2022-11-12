from django.shortcuts import render
from .models import Department, Department_user
from Janta.models import Complaint
# Create your views here.

def login(request):
    return render(request, 'department/login.html')

def dashboard(request , dept):

    Dept_usr = Department_user.objects.filter(user=request.user , department__name__contains = dept)

    Complaints = Complaint.objects.filter(department = Dept_usr[0].department)

    return render(request, 'department/dashboard.html' , {'dept':dept , 'complaints':Complaints})


def resolved(request , dept):

    Dept_usr = Department_user.objects.filter(user=request.user , department__name__contains = dept)

    Complaints = Complaint.objects.filter(department = Dept_usr[0].department , status = '5')
    print(Complaints)
    return render(request, 'department/resolved.html' , {'dept':dept , 'complaints':Complaints})

def compdet(request , dept , uuid):
    Dept_usr = Department_user.objects.filter(user=request.user , department__name__contains = dept)
    Complaints = Complaint.objects.filter(department = Dept_usr[0].department , Uuid = uuid)[0]

    

    return render(request, 'department/compdet.html' , {'dept':dept , 'comp':Complaints})
    