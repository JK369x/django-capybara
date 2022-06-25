from django.contrib import admin
from .models import *

admin.site.register(Product) #ทำให้ admin สามารถเห็น data base ของเรา
admin.site.register(ContactUs)
admin.site.register(Profile)