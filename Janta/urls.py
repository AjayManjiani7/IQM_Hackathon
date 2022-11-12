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
]