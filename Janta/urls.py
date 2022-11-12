from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('login' , views.login , name='login'),

    path('register' , views.register , name='register'),

    path('Complaint' , views.Complaint , name='Complaint'),

    path('dashboard' , views.dashboard , name='dashboard'),

    path('status' , views.status , name='status'),
]