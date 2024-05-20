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
from .models import Booking

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
def select_payment(request):
    booking_id = request.session.get('booking_id')
    try:
        user = Customer.objects.get(user=request.user)
        booking = Booking.objects.get(id=booking_id)
        booking.customer_id == user.user_id
    except ObjectDoesNotExist:
        return redirect('go_home')
    
    if not booking_id:
        messages.error(request, 'No booking found in session.')
        return redirect('home')
    
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'select_payment.html', {'price': booking.price})

def create_payment(request):
    booking_id = request.session['booking_id']

    try:
        user = Customer.objects.get(user=request.user)
        booking = Booking.objects.get(id=booking_id)
        if booking.payment_method:
            return redirect('payment_status', booking_id=booking.id)
        booking.customer_id == user.user_id
    except ObjectDoesNotExist:
        return redirect('go_home')
    if not booking_id:
        messages.error(request, 'No booking found in session.')
        return redirect('go_home')
    
    booking = Booking.objects.get(id=booking_id)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        transfer_receipt = request.FILES.get('transfer_receipt')

        if payment_method:
            booking.payment_method = payment_method
            if payment_method == 'bank_transfer':
                if transfer_receipt:
                    booking.transfer_receipt = transfer_receipt
                    booking.payment_status = 'pending'  # Set to pending until verified
                    booking.save()
                    return redirect('payment_pending')
                else:
                    messages.error(request, 'Please upload the transfer receipt.')
            elif payment_method == 'cash':
                booking.payment_status = 'pending'  # Assume cash payment is immediate
                booking.save()
                return redirect('payment_pending')
        else:
            messages.error(request, 'Please select a payment method.')
    
    return render(request, 'booking/payment_form.html', {'price': booking.price})

def payment_status(request, booking_id):
    booking_id = request.session['booking_id']
    booking = Booking.objects.get(id=booking_id)
    if booking.payment_status == "completed":
        return redirect('payment_success', booking_id)
    if booking.payment_status == "pending":
        return redirect('payment_pending', booking_id)
    if booking.payment_status == "declined":
        return redirect('payment_declined', booking_id)


def payment_success(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request, 'booking/payment_success.html', {'booking':booking})

def payment_pending(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request,'booking/payment_pending.html', {'booking':booking})

def payment_declined(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    return render(request,'booking/payment_declined.html', {'booking':booking})



    
