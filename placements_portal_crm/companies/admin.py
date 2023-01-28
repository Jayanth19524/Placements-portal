from django.contrib import admin

# Register your models here.
from .models import Csedata,Mechdata,EEEdata,Civildata
admin.site.register(Csedata)
admin.site.register(Civildata)
admin.site.register(Mechdata)
admin.site.register(EEEdata)
