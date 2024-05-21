from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import User, Driver, Customer
from booking.models import Booking
from vehicles.models import Truck, TruckForm, Maintenance
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_GET
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
    
def history(request):
    if not request.user.is_authenticated:
        return redirect('go_home')
    if request.user.is_customer:
        return redirect('customer_bookings')
    elif request.user.is_superuser:
        return redirect(request, 'admin/base_site.html')
    elif request.user.is_driver:
        return redirect('driver_bookings')
    
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
    try: #Check whether the driver is already accepted or not
        user_driver = Driver.objects.get(user=request.user.user_driver)
        if user_driver.accepted != 1: #If not accepted, redirect to the registration thanks page
         return render(request, 'pages/registration_thanks.html')
    except ObjectDoesNotExist:
        #Now, if the driver not NOT Accepted, redirect to the home page
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
@user_passes_test(im_driver, login_url='/')
def save_truck(request):
    try:
        driver = Driver.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Handle the case where the driver does not exist
        return redirect('go_home')
    
    truck_id = request.session['truck_id']
    truck = Truck.objects.get(id=truck_id)
    if truck.driver_id != driver.user_id:
        return redirect('driver_trucks')
    
    
    if request.method == 'POST':
        if 'overall_view' in request.FILES:
            truck.overall_view = request.FILES['overall_view']
        if 'front_view' in request.FILES:
            truck.front_view = request.FILES['front_view']
        if 'side_view' in request.FILES:
            truck.side_view = request.FILES['side_view']
        if 'back_view' in request.FILES:
            truck.back_view = request.FILES['back_view']
        if 'top_view' in request.FILES:
            truck.top_view = request.FILES['top_view']
        truck.model = request.POST['truck_model']
        truck.license_plate = request.POST['license_plate']
        truck.capacity = request.POST['capacity']
        truck.truck_available = request.POST['truck_available']
        truck.save()
            
    return redirect('edit_truck', truck_id)
@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/')
@require_GET
def edit_truck(request, truck_id):
    try:
        driver = Driver.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Handle the case where the driver does not exist
        return redirect('go_home')
    
    request.session['truck_id'] = truck_id
    truck = Truck.objects.get(id=truck_id)
    if truck.driver_id != driver.user_id:
        return redirect('driver_trucks')
    
    request.session['truck_model'] = truck.truck_model
    request.session['license_plate'] = truck.license_plate
    request.session['driver'] = truck.driver.username() if truck.driver else None
    request.session['capacity'] = truck.capacity
    request.session['location'] = truck.location
    request.session['status'] = truck.status
    request.session['last_maintained'] = truck.last_maintained.isoformat() if truck.last_maintained else None
    request.session['front_view'] = truck.front_view.url if truck.front_view else None
    request.session['side_view'] = truck.side_view.url if truck.side_view else None
    request.session['back_view'] = truck.back_view.url if truck.back_view else None
    request.session['top_view'] = truck.top_view.url if truck.top_view else None
    request.session['overall_view'] = truck.overall_view.url if truck.overall_view else None
    request.session['truck_accepted'] = truck.truck_accepted
    request.session['truck_available'] = truck.truck_available
    # truck_id = request.GET.get('id')
    # truck = get_object_or_404(Truck, id=truck_id)
    # data = {
    #         'truck_model': truck.truck_model,
    #         'capacity': truck.capacity,
    #         'license_plate': truck.license_plate,
    #         'status': truck.status,
    #         'last_maintained': truck.last_maintained.isoformat(),
    #         'truck_available': truck.truck_available,
    #         'truck_accepted': truck.truck_accepted,
    #         'driver': truck.driver.id,
    #         'overall_view': truck.overall_view.url,
    #         'front_view': truck.front_view.url,
    #         'side_view': truck.side_view.url,
    #         'back_view': truck.back_view.url,
    #         'top_view': truck.top_view.url,
    #     }
    # return JsonResponse(data)
    return render(request, 'pages/trucks/driver/edit_truck.html' )
    

@login_required(login_url = 'login')
@user_passes_test(im_customer, login_url='/')
# @user_passes_test(initely, login_url='/login')
def customer_trucks(request):
    try: #Check whether the driver is already accepted or not
        user = Customer.objects.get(user=request.user)
    except ObjectDoesNotExist:
        #Now, if the driver not NOT Accepted, redirect to the home page
        return redirect('go_home')
    trucks = Truck.objects.filter(truck_available=1)
    return render(request, 'pages/trucks/customer/customer_truck.html', {'trucks': trucks})

@login_required(login_url = 'login')
@user_passes_test(im_customer, login_url='/')
# @user_passes_test(initely, login_url='/login')
def booking(request, truck_id):
    try: #Check whether the driver is already accepted or not
        user = Customer.objects.get(user=request.user)
    except ObjectDoesNotExist:
        #Now, if the driver not NOT Accepted, redirect to the home page
        return redirect('go_home')

    truck = Truck.objects.get(id=truck_id)
    request.session['truck_id']=truck_id
    return render(request, 'booking/booking_customer.html', {'truck': truck})

@login_required(login_url='login')
@user_passes_test(im_customer, login_url='/')
def book_truck(request):
    try:
        # Check whether the user is a Customer
        user = Customer.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Redirect to the home page if the user is not a Customer
        return redirect('go_home')

    truck_id = request.session.get('truck_id')
    if not truck_id:
        return redirect('go_home')  # Handle the case where truck_id is not in session

    try:
        truck = Truck.objects.get(id=truck_id)
    except Truck.DoesNotExist:
        return redirect('go_home')  # Handle the case where truck does not exist

    if request.method == 'POST':
        pickup = request.POST['pickup']
        destination = request.POST['destination']
        distance = request.POST['distance']
        date = request.POST['date']
        details = request.POST['details']
        weight = request.POST['weight']
        price = request.POST['price']
        truck.truck_available=0

        # Store the form data in session (optional)
        request.session['pickup'] = pickup
        request.session['destination'] = destination
        request.session['distance'] = distance
        request.session['date'] = date
        request.session['details'] = details
        request.session['weight'] = weight
        request.session['price'] = price

        # Create and save the booking
        truck.save()
        booking = Booking.objects.create(
            pickup=pickup,
            destination=destination,
            distance=distance,
            date=date,
            details=details,
            weight=weight,
            customer=user,
            driver=truck.driver,
            truck=truck,
            price=price
        )

        # Redirect to the booking result with the booking_id
        return redirect('booking_result', booking_id=booking.id)

    return redirect('go_home')

@login_required(login_url = 'login')
# @user_passes_test(initely, login_url='/login')
def booking_result(request, booking_id):
    if request.user.is_customer:
        try:
            user = Customer.objects.get(user=request.user)
            booking = Booking.objects.get(id=booking_id)
            # booking.customer_id == user.id
            truck = Truck.objects.get(id=booking.truck_id)
            
        except ObjectDoesNotExist:
            return redirect('go_home')
    elif request.user.is_driver:
        try:
            user = Driver.objects.get(user=request.user)
            booking = Booking.objects.get(id=booking_id)
            # booking.driver_id == user.id
            truck = Truck.objects.get(id=booking.truck_id)
            customer = Customer.objects.get(id = booking.customer_id)
            
        except ObjectDoesNotExist:
            return redirect('go_home')
    
    request.session['booking_id']=booking_id
    request.session['truck_id']=truck.id
    request.session['pickup'] = booking.pickup
    request.session['destination'] = booking.destination
    request.session['distance'] = booking.distance
    request.session['date'] = booking.date.strftime('%Y-%m-%d')
    request.session['details'] = booking.details
    request.session['weight'] = booking.weight
    request.session['price'] = booking.price
    
    return render(request, 'booking/booking_result.html', {'booking': booking, 'truck':truck, 'customer': customer})


@login_required(login_url = 'login')
@user_passes_test(im_customer, login_url='/')
def history_customer(request):
    bookings = Booking.objects.filter(customer_id=request.user.id)
    return render(request, 'b_history/booking-history_customer.html',{'bookings':bookings})



@login_required(login_url = 'login')
@user_passes_test(im_driver, login_url='/')
def history_driver(request):
    bookings = Booking.objects.filter(driver_id=request.user.id)
    return render(request, 'b_history/booking_driver.html',{'bookings':bookings})