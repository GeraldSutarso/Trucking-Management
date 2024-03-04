from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import User, Driver, Customer
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

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
    if not request.user.is_authenticated:
        return redirect('go_home')
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
# def initely(request):
    # user_driver = Driver.objects.get(user_id=User.id)
    # user_driver.accepted == 1:
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
@user_passes_test(im_driver, login_url='/login')
def driver_home(request):
    user_driver = Driver.objects.get(user_id=request.user.id)
    if user_driver.accepted != 1:
        return render(request, 'pages/registration_thanks.html')
    print("User:", request.user)
    # print("Driver:", request.Driver)
    return render(request, 'pages/driver_home.html')

@login_required(login_url = 'login')
@user_passes_test(im_customer, login_url='/')
def customer_home(request):
    return render(request, 'pages/customer_home.html')



#profile
@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/')
# @user_passes_test(initely, login_url='/login')
def driver_profile(request):
    return render(request, 'pages/profile/driver_profile.html')

@login_required(login_url = 'login')
@user_passes_test(im_customer, login_url='/')
def customer_profile(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Handle the case where the customer does not exist
        return redirect('go_home')

    # Save the customer's data in the session
    request.session['firstname'] = customer.first_name()
    request.session['lastname'] = customer.last_name()
    request.session['username'] = customer.username()
    request.session['phone_number'] = customer.phone_number()
    request.session['email'] = customer.email()
    request.session['address'] = customer.address
    request.session['profile_picture'] = customer.profile_picture.url if customer.profile_picture else None

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']

        if User.objects.filter(username=username).exclude(username=request.user.username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('customer_profile')
        else:
            if User.objects.filter(email=email).exclude(email=request.user.email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('customer_profile')
            else:
                request.user.first_name = firstname
                request.user.last_name = lastname
                request.user.email = email
                request.user.phone_number = phone_number
                request.user.username = username
                request.user.save()

                customer.address = address
                # Assuming the profile picture is being sent in the 'profile_picture' field
                if 'profile_picture' in request.FILES:
                    customer.profile_picture = request.FILES['profile_picture']
                customer.save()

                messages.success(request, 'Profile updated successfully.')
                return redirect('customer_profile')

    return render(request, 'pages/profile/customer_profile.html')