from django.shortcuts import render, redirect
from .models import Soldat, Geroy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout

def popular_list(request):
    geroy = Geroy.objects.filter(available=True)[3:]
    return render(request,'main/index/index.html',{'geroy':geroy})


def geroy_detail(request,slug):
    return render(request,'main/product/detail.html')

def register(request):
    return render(request,'main/auth/register.html')

def authtorisation(request):
    return render(request,'main/auth/authtorisation.html')


def login(request):
    return render(request,'main/accounts/login.html')