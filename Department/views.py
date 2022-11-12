from django.shortcuts import render , redirect
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

def update(request , dept , uuid):
    Dept_usr = Department_user.objects.filter(user=request.user , department__name__contains = dept)
    comp = Complaint.objects.filter(department = Dept_usr[0].department , Uuid = uuid)[0]

    if request.method == 'POST':
        status = request.POST.get('status')
        public = request.POST.get('public') == 'on'

        comp.status = status
        if public:
            comp.public = True
        else:
            comp.public = False

        if status == '1':
            comp.status_com_1 = request.POST.get('sub_comment')
        elif status == '2':
            comp.status_com_2 = request.POST.get('ver_comment')
        elif status == '3':
            comp.status_com_3 = request.POST.get('ass_comment')
        elif status == '4':
            comp.status_com_4 = request.POST.get('pro_comment')
        elif status == '5':
            comp.status_com_5 = request.POST.get('res_comment')
                  

        comp.save()

    return redirect('compdet' , dept = dept , uuid = uuid)