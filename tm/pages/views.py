from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import User, Driver
from django.contrib.auth.decorators import login_required, user_passes_test

# FALL BACKK!! FALL BACKK!!!
def go_home(request):
    if request.user.is_authenticated:
        if request.user.is_customer: # check if the user is a customer
            return redirect('customer_home')
        elif request.user.is_superuser: # check if the user is a superuser
            return render(request, 'admin/base_site.html')
        elif request.user.is_driver: 
            return redirect('driver_home')
    else:
        request.session.flush()
        return render(request,'pages/no_home.html')
def profile(request):
    if request.user.is_authenticated:
        if request.user.is_customer:
            return redirect('customer_profile')
        elif request.user.is_superuser:
            return redirect(request, 'admin/base_site.html')
        elif request.user.is_driver:
            return redirect('driver_profile')
        
#HEY USER, WHO ARE YOU??

def im_customer(user):
    # return hasattr(user, is_customer=1)
    return user.is_customer
def im_superman(user):
    # return hasattr(user, is_superuser=1)
    return user.is_superuser
def im_driver(user):
    # return hasattr(user, is_driver=1)
    return user.is_driver

#Oi, Are you accepted?
def initely(request,user, Driver):
    return request.user.Driver.accepted
#other redirectings
def go_login(request):
    return redirect('login')

def go_logout(request):
    return redirect('logout')

def go_register_c(request):
    return redirect('register_customer')

def go_register_d(request):
    return redirect('register_driver')

#home
@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/laogin')
@user_passes_test(initely, login_url='logain')
def driver_home(request):
    return render(request, 'pages/driver_home.html')

@login_required(login_url = 'login')
@user_passes_test(im_customer, login_url='/')
def customer_home(request):
    return render(request, 'pages/customer_home.html')



#profile
@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/')
@user_passes_test(initely, login_url='/login')
def driver_profile(request):
    return render(request, 'pages/profile/driver_profile.html')

@login_required(login_url = 'login')
@user_passes_test(im_customer, login_url='/')
def customer_profile(request):
    return render(request, 'pages/profile/customer_profile.html')