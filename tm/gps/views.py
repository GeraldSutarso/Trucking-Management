# In gps/views.py

from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User, Driver, Customer
from django.contrib.auth.decorators import login_required, user_passes_test

def im_customer(user):
    return user.is_customer
def im_superman(user):
    return user.is_superuser
def im_driver(user):
    return user.is_driver

@login_required(login_url='login')
def gps(request):
    # Your view logic goes here
    return render(request,"gps/gps.html")



