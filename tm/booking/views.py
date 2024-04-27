from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import User, Driver, Customer
from vehicles.models import Truck, TruckForm, Maintenance
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_GET
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

@login_required(login_url = 'login')
@user_passes_test(im_customer, login_url='/')
def customer_booking(request):
    
    return render(request,'booking/booking_customer.html')
    