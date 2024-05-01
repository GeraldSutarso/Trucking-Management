from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import User, Driver, Customer
from vehicles.models import Truck, TruckForm, Maintenance
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# FALL BACKK!! FALL BACKK!!! HANDLE WHICH TYPE IS THE USER
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
    
def trucks(request):
    if not request.user.is_authenticated:
        return redirect('go_home')
    if request.user.is_customer:
        return redirect('customer_trucks')
    elif request.user.is_superuser:
        return redirect(request, 'admin/base_site.html')
    elif request.user.is_driver:
        return redirect('driver_trucks')
    
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

    driver = Driver.objects.get(user=request.user)
    # Save the driver's data in the session
    request.session['firstname'] = driver.first_name()
    request.session['lastname'] = driver.last_name()
    request.session['username'] = driver.username()
    request.session['phone_number'] = driver.phone_number()
    request.session['email'] = driver.email()
    request.session['license_number'] = driver.license_number
    request.session['availability'] = driver.availability
    request.session['profile_picture'] = driver.profile_picture.url if driver.profile_picture else None
    request.session['id_card'] = driver.id_card.url if driver.id_card else None
    request.session['license_card'] = driver.license_card.url if driver.license_card else None
    request.session['profile_picture_confirmed'] = driver.profile_picture_confirmed
    request.session['accepted'] = driver.accepted
    request.session['vehicle_available'] = driver.vehicle_available
    # print("Driver:", request.Driver)
    return render(request, 'pages/driver_home.html')

@login_required(login_url = 'login')
@user_passes_test(im_customer, login_url='/')
def customer_home(request):
    # get session for customer
    customer = Customer.objects.get(user=request.user)
    request.session['firstname'] = customer.first_name()
    request.session['lastname'] = customer.last_name()
    request.session['username'] = customer.username()
    request.session['phone_number'] = customer.phone_number()
    request.session['email'] = customer.email()
    request.session['address'] = customer.address
    request.session['profile_picture'] = customer.profile_picture.url if customer.profile_picture else None
    return render(request, 'pages/customer_home.html')



#profile
@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/')
# @user_passes_test(initely, login_url='/login')
def driver_profile(request):
    try:
        driver = Driver.objects.get(user=request.user)
        if driver.accepted != 1:
         return render(request, 'pages/registration_thanks.html')
    except ObjectDoesNotExist:
        # Handle the case where the driver does not exist
        return redirect('go_home')

    # Save the driver's data in the session
    request.session['firstname'] = driver.first_name()
    request.session['lastname'] = driver.last_name()
    request.session['username'] = driver.username()
    request.session['phone_number'] = driver.phone_number()
    request.session['email'] = driver.email()
    request.session['license_number'] = driver.license_number
    request.session['availability'] = driver.availability
    request.session['profile_picture'] = driver.profile_picture.url if driver.profile_picture else None
    request.session['id_card'] = driver.id_card.url if driver.id_card else None
    request.session['license_card'] = driver.license_card.url if driver.license_card else None
    request.session['profile_picture_confirmed'] = driver.profile_picture_confirmed
    request.session['accepted'] = driver.accepted
    request.session['vehicle_available'] = driver.vehicle_available
    
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        if User.objects.filter(email=email).exclude(email=request.user.email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('driver_profile')
        else:
            request.user.first_name = firstname
            request.user.last_name = lastname
            request.user.email = email
            request.user.phone_number = phone_number
            request.user.username = username
            request.user.save()

            driver.license_number = request.POST['license_number']
            driver.availability = request.POST['availability']

            # Assuming the profile picture, id card, and license card are being sent in the respective fields
            if 'profile_picture' in request.FILES:
                driver.profile_picture = request.FILES['profile_picture']
            if 'id_card' in request.FILES:
                driver.id_card = request.FILES['id_card']
            if 'license_card' in request.FILES:
                driver.license_card = request.FILES['license_card']
            driver.save()

            messages.success(request, 'Profile updated successfully.')
            return redirect('driver_profile')

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

#Trucks
@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/')
# @user_passes_test(initely, login_url='/login')
def driver_trucks(request):
    try:
        user_driver = Driver.objects.get(user=request.user.user_driver)
        if user_driver.accepted != 1:
         return render(request, 'pages/registration_thanks.html')
    except ObjectDoesNotExist:
        # Handle the case where the driver does not exist
        return redirect('go_home')
    current_driver_trucks = Truck.objects.filter(driver=request.user.user_driver)
    other_driver_trucks = Truck.objects.exclude(driver=request.user.user_driver) #.exclude(truck_available=False).exclude(truck_accepted=False).exclude(driver__availability=False).exclude(driver__profile_picture_confirmed=False)
    return render(request, 'pages/trucks/driver/driver_truck.html', {'current_driver_trucks': current_driver_trucks, 'other_driver_trucks': other_driver_trucks})

@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/')
@csrf_exempt
def delete_truck(request):
    if request.method == 'POST':
        truck_id = request.POST.get('truck_id')
        Truck.objects.filter(id=truck_id).delete()
        return JsonResponse({'status':'success'})    

@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/')
def add_truck(request):
    if request.method == 'POST':
        form = TruckForm(request.POST, request.FILES)
        if form.is_valid():
            if form.is_valid():
                truck = form.save()

                return JsonResponse({
                    'status': 'success',
                    'truck': {
                        'id': truck.id,
                        'overall_view_url': truck.overall_view.url,
                        'front_view_url': truck.front_view.url,
                        'side_view_url': truck.side_view.url,
                        'back_view_url': truck.back_view.url,
                        'top_view_url': truck.top_view.url,
                        'truck_available': truck.truck_available,
                        'truck_accepted': truck.truck_accepted,
                        'status': truck.status,
                        'truck_model': truck.truck_model,
                        'license_plate': truck.license_plate,
                        'capacity': truck.capacity,
                    }
                })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = TruckForm()
    return render(request, 'driver/driver_truck.html', {'form': form})
@login_required(login_url = 'login')
@user_passes_test(im_customer, login_url='/')
# @user_passes_test(initely, login_url='/login')
def customer_trucks(request):
    return render(request, 'pages/trucks/customer/customer_truck.html')