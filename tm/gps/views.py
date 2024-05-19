# In gps/views.py

from django.shortcuts import render
from django.http import HttpResponse

def gps(request):
    # Your view logic goes here
    return render(request,"gps/gps.html")
