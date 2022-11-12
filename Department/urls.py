from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('/login' , views.login , name='login'),

    path('/dashboard/<str:dept>' , views.dashboard , name='dashboard'),
    path('/dashboard/<str:dept>/resolved' , views.resolved , name='resolved'),
    # path('/dashboard/<str:dept>/details' , views.dashboard , name='dashboard'),
    path('/dashboard/<str:dept>/comp/<str:uuid>' , views.compdet , name='compdet'),
    path('/dashboard/<str:dept>/comp/<str:uuid>/update' , views.update , name='update'),
]