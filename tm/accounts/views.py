from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import User, Driver
from pages.urls import urlpatterns
from django.contrib.auth.decorators import login_required

def login(request):
    if request.user.is_authenticated:
        return redirect ('go_home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user1 = auth.authenticate(username=username, password=password, is_superuser = 1)
        user2 = auth.authenticate(username=username, password=password, is_customer = 1)
        user3 = auth.authenticate(username=username, password=password, is_driver = 1)
        if user1 is not None: 
            messages.success(request, 'You are an admin! Please login from the admin page')
            return render(request, 'admin/base_site.html')
        elif user2 is not None:
            messages.success(request, 'You are now logged in.')
            return redirect('go_customer_home')
        elif user3 is not None:
            messages.success(request, 'You are now logged in.')
            return redirect('go_driver_home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
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
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,phone_number = phone_number , username=username, password=password, is_customer = True)
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('go_customer_home')

        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
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

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,phone_number = phone_number , username=username, password=password, is_driver = True)
                    driver = Driver.objects.create(id_card = id_card, license_card = license_card)
                    user.save()
                    driver.save()
                    messages.success(request, 'You are registered successfully. Please wait for confirmation from the admin.')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register_customer.html')

@login_required(login_url = 'login')
def go_driver_home(request):
    return redirect(request, 'go_home')

@login_required(login_url = 'login')
def go_customer_home(request):
    return redirect(request, 'go_home')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')

@login_required(login_url = 'login')
def admin(request):
    return render(request, 'admin/base_site.html')

