from django.shortcuts import render , redirect
from .models import Complaint
from Department.models import Department , Department_user

# Create your views here.
def login(request):
    return render(request, 'janta/login.html')

def register(request):
    return render(request, 'janta/register.html')


def complaint(request):
    return render(request, 'janta/complaint.html')

def dashboard(request):
    return render(request, 'janta/dashboard.html')

def status(request):
    return render(request, 'janta/status.html')

# CRUD Oprations for users
# 

def create_comp(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        severity = request.POST.get('severity')
        dept = request.POST.get('dept')
        desc = request.POST.get('desc')
        photo1 = request.FILES.get('photo')
        location = request.POST.get('location')
        send_copy = request.POST.get('send_copy') == 'on'
        print(title , severity , dept , send_copy , desc , location)

        Department_obj = Department.objects.filter(name = dept.capitalize())
        if Department_obj is not None:
            print("Department Found")
            Complaint_obj = Complaint(User = request.user , title = title , severity = severity , department = Department_obj[0] , description = desc , image = photo1 , location = location , send_to_email = send_copy)
            Complaint_obj.save()

            return redirect('dashboard')
        # return redirect('dashboard')