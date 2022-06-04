from django.contrib import admin
from .models import *

from django.contrib.auth.models import User


if User == True:
            User.is_staff = True
            User.is_superuser=True
          




# Register your models here.
admin.site.register(Person)


    


        
