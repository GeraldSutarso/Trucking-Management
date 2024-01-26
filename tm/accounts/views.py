from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import User, Driver, Customer
from pages.urls import urlpatterns
from django.contrib.auth.decorators import login_required

def login(request):
    if request.user.is_authenticated:
        return redirect ('go_home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        request.session['username'] = username
        
        
        user = auth.authenticate(username=username, password=password)
        if username is None:
                messages.error(request, 'Invalid username')
                return redirect('login')
        else:
            if password is None:
                messages.error(request, 'Invalid password')
                return redirect('login')
            elif user.is_superuser: 
                messages.error(request, 'You are an admin! Please login from the admin page')
                return render(request, 'admin/base_site.html')
            elif user.is_customer:
                # messages.success(request, 'You are now logged in.')
                return redirect('customer_home')
            elif user.is_driver:
                user_driver = Driver
                if user_driver.accepted:
                # messages.success(request, 'You are now logged in.')
                    return redirect('driver_home')


    return render(request, 'accounts/login.html')

def register_customer(request):
    if request.user.is_authenticated:
        return redirect ('go_home')
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        # address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        request.session['firstname'] = firstname
        request.session['lastname'] = lastname
        request.session['username'] = username
        request.session['phone_number'] = phone_number
        request.session['email'] = email
        # request.session['address'] = address
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register_customer')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register_customer')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,phone_number = phone_number , username=username, password=password, is_customer = True)
                    user.save()
                    customer = Customer.objects.create(user=user)
                    customer.save()
                #   messages.success(request, 'You are registered successfully.')
                    auth.login(request, user)
                    # messages.success(request, 'You are now logged in.')
                    return redirect('customer_home')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register_customer')
    
    return render(request, 'accounts/register_customer.html')

def register_driver(request):
    if request.user.is_authenticated:
        return redirect ('go_home')
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        phone_number = request.POST['phone_number']
        id_card = request.POST['id_card']
        license_card = request.POST['license_card']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        request.session['firstname'] = firstname
        request.session['lastname'] = lastname
        request.session['username'] = username
        request.session['phone_number'] = phone_number
        request.session['email'] = email
        request.session['id_card'] = id_card
        request.session['license_card']=license_card

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register_driver')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register_driver')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,phone_number = phone_number , username=username, password=password, is_driver = True)
                    user.save()
                    driver = Driver.objects.create(user= user,id_card = id_card, license_card = license_card)
                    driver.save()
                    # messages.success(request, 'You are registered successfully. Please wait for confirmation from the admin.')
                    return render(request, 'pages/registration_thanks.html')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register_driver')
    
    return render(request, 'accounts/register_driver.html')

def logout(request):
    # if request.method == 'POST':
        auth.logout(request)
        request.session.flush()
        return redirect('go_home')
    # return redirect('go_home')

@login_required(login_url = 'login')
def admin(request):
    return render(request, 'admin/base_site.html')

