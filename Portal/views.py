from django.shortcuts import render
from Janta.models import Complaint

# Create your views here.


def home(request):
    ed_st = len(Complaint.objects.filter(department__name__contains = 'education'))
    sp_st = len(Complaint.objects.filter(department__name__contains = 'Sports'))
    fc_st = len(Complaint.objects.filter(department__name__contains = 'Finance'))
    ag_st = len(Complaint.objects.filter(department__name__contains = 'Agriculture'))
    wc_st = len(Complaint.objects.filter(department__name__contains = 'Women and Child Development'))
    
    pie = {'ed_st':ed_st , 'sp_st':sp_st , 'fc_st':fc_st , 'ag_st':ag_st , 'wc_st':wc_st}

    sb = len(Complaint.objects.filter(status = '1'))
    vr = len(Complaint.objects.filter(status = '2'))
    ass = len(Complaint.objects.filter(status = '3'))
    pr = len(Complaint.objects.filter(status = '4'))
    rs = len(Complaint.objects.filter(status = '5'))

    grphi = {'sb':sb , 'vr' : vr , 'ass' : ass , 'pr' : pr , 'rs' : rs}

    return render(request, 'portal/home.html' , {'pie':pie , 'grphi':grphi})

def faq(request):
    return render(request, 'portal/faq.html')    
