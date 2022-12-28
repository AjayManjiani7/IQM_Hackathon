import json
from django.shortcuts import render , redirect
from .models import Complaint
from django.http import HttpResponse , JsonResponse
from Department.models import Department , Department_user
import requests
from django.conf import settings
from django.core.mail import send_mail

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
        print(title , severity , dept , send_copy , desc , location ,aadhaar)

        Department_obj = Department.objects.filter(name = dept.capitalize())
        if Department_obj is not None:
            print("Department Found")
            Complaint_obj = Complaint(full_name = fullname, email = email ,phone = phone , adhaar_number = aadhaar , title = title , severity = severity , department = Department_obj[0] , description = desc , image = photo1 , location = location , send_to_email = send_copy)
            Complaint_obj.save()

            # Email Copy
            subject = 'Complaint Copy'
            message = f'title : {title} \n severity : {severity} \n department : {dept} \n description : {desc} \n location : {location} \n'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )

            return redirect('complaint_submitted/'+ str(Complaint_obj.Uuid))
        else :
            print("Department Not Found")
            return redirect('complaint')
        # return redirect('dashboard')

def status(request , idcomplain):
    complain = Complaint.objects.filter(Uuid = idcomplain)
    if complain is not None:
        return render(request , 'janta/status.html' , {'comp' : complain[0]})
    else :
        return redirect('home')


def send_otp(request , no):
    mobile = no
    a = requests.get('https://2factor.in/API/V1/YOUR-API-KEY-HERE/SMS/' + str(mobile) + '/AUTOGEN')
    b = json.loads(a.text)
    id = b['Details']

    print(id)
    return JsonResponse({'id': id})

def verify_otp(request , id , otp):
    session_id =id
    c = requests.get('https://2factor.in/API/V1/YOUR-API-KEY-HERE/SMS/VERIFY/'+ session_id + '/' + otp)
    d = json.loads(c.text)

    if d['Details'] == 'OTP Matched':
        return JsonResponse({'value': 'true'})
    else:
        return JsonResponse({'value': 'false'})


def public(request):
    complaints = Complaint.objects.filter(public = True)

    return render(request , 'janta/public.html' , {'comps' : complaints})
