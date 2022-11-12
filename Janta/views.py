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

def complaint_submitted(request , idcomplain):

    # complains = Complaint.objects.filter(User = request.user)
    # print(complains)
    return render(request, 'janta/complaint_Submitted.html' , {'complain_id' : idcomplain})

def status(request):
    return render(request, 'janta/status.html')

# CRUD Oprations for users
# 

def create_comp(request):
    if request.method == 'POST':

        fullname = request.POST.get('fullname')
        aadhaar = request.POST.get('aadhaar')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

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
            Complaint_obj = Complaint(full_name = fullname, email = email ,phone = phone , adhaar_number = aadhaar , title = title , severity = severity , department = Department_obj[0] , description = desc , image = photo1 , location = location , send_to_email = send_copy)
            Complaint_obj.save()

            return redirect('dashboard')
        else :
            print("Department Not Found")
            return redirect('create_comp')
        # return redirect('dashboard')