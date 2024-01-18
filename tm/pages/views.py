from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import User, Driver
from django.contrib.auth.decorators import login_required

# Create your views here.
def go_home(request):
    return redirect('customer_home')

def go_login(request):
    return redirect('login')

def go_register_c(request):
    return redirect('register_customer')

def go_register_d(request):
    return redirect('register_driver')

@login_required(login_url = 'login')
def driver_home(request):
    return render(request, 'pages/driver_home.html')

@login_required(login_url = 'login')
def customer_home(request):
    return render(request, 'pages/customer_home.html')