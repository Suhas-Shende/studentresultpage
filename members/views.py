from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from members.decorators import unauthenticated_user
# from django.contrib.auth.models import include_superusers
from django.contrib.auth.models import Group
# Create your views here.
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

from .models import *
@unauthenticated_user
def registerpage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')
	# else:
         form=UserCreationForm()
         if request.method =="POST":
             form = UserCreationForm(request.POST )
             if form.is_valid():
                    
                   
                    user=form.save()
                    user.is_active = True
                    user.is_staff=True
                   
                    user.is_superuser = True
                    user.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, 'Profile details updated.'+username)
                    group = Group.objects.get(name='teacher')
                    user.groups.add(group)
                    return redirect('userpage')
         context={'form':form}
         return render(request,'register.html',context)


@unauthenticated_user
def registerpagestudent(request):

         form=UserCreationForm()
         if request.method =="POST":
             form = UserCreationForm(request.POST )
             if form.is_valid():
                    
                   
                    user=form.save()
                    user.is_active = True
                    user.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, 'Profile details updated.'+username)
                    group = Group.objects.get(name='student')
                    user.groups.add(group)
                    return redirect('login')
         context={'form':form}
         return render(request,'registerstudent.html',context)

@unauthenticated_user
def loginPage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')
	# else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password =request.POST.get('password')
              
                user = authenticate(request, username=username, password=password)
                
                
                if user is not None:
                    login(request, user)
                    return redirect('login')
                else:
                    messages.info(request, 'Username OR password is incorrect')

            context = {}
            return render(request, 'login.html', context)
          
def logoutUser(request):
	
    
    logout(request)

    return redirect('login')


def logoutUserr(request):
	logout(request)
   
	return redirect('userpage')

def userpage (request):
        if request.user.is_authenticated:
            return redirect('search-venues')
        else:
         if request.method == 'POST':
                username = request.POST.get('username')
                password =request.POST.get('password')
              
                user = authenticate(request, username=username, password=password)
              
                
                if user is not None:
                    login(request, user)
                    return redirect('userpage')
                else:
                    messages.info(request, 'Username OR password is incorrect')

           
         context={}
         return render(request,'user.html',context)

def PasswordChangeView(request):
    # form=PasswordChangeForm(PasswordChangeView)
    form=PasswordChangeForm(request)
    if request.method =="POST":
       
        if form.is_valid():
            form.set_password('new password')
            form.save()
            # messages.success(request, 'Created successfully.')
            # return redirect ('search-venues')
    context={'form':form}
    return render(request,'changepass.html',context)