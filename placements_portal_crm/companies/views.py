from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'companies/home.html')
def dashboard(request):
    companies = Csedata.objects.all()
    return render(request,'companies/dashboard.html',{'companies':companies})
def mechdashboard(request):
    mechcompanies = Mechdata.objects.all()
    return render(request,'companies/mechdashboard.html',{'mechcompanies':mechcompanies})
def civildashboard(request):
    civilcompanies = Civildata.objects.all()
    return render(request,'companies/civildashboard.html',{'civilcompanies':civilcompanies})
def eeedashboard(request):
    eeecompanies = EEEdata.objects.all()
    return render(request,'companies/eeedashboard.html',{'eeecompanies':eeecompanies})
