from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('eeedashboard/',views.eeedashboard),
    path('civildashboard/',views.civildashboard),
    path('mechdashboard/',views.mechdashboard),
]