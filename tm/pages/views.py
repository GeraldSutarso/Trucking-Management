from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import User, Driver
from django.contrib.auth.decorators import login_required

# FALL BACKK!! FALL BACKK!!!
def go_home(request):
    if request.user.is_authenticated:
        if request.user.is_staff: # check if the user is a staff member
            return redirect('customer_home')
        elif request.user.is_superuser: # check if the user is a superuser
            return redirect('admin')
        else: # assume the user is a driver by default
            return redirect('driver_home')
    else:
        return render(request,'pages/no_home.html')


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