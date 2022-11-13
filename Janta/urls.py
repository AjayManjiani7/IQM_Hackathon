from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('/login' , views.login , name='login'),

    path('/register' , views.register , name='register'),

    path('/complaint' , views.complaint , name='complaint'),

    path('/complaint_submitted/<str:idcomplain>' , views.complaint_submitted , name='complaint_submitted'),

    path('/create_comp' , views.create_comp , name='create_comp'),

    path('/status/<str:idcomplain>' , views.status , name='status'),

    path('/public' , views.public , name='public'),

    # OTP
    path('/send_otp/<str:no>' , views.send_otp , name='send_otp'),
    path('/verify_otp/<str:id>/<str:otp>' , views.verify_otp , name='verify_otp'),
]