# from _typeshed import Self
from typing import _SpecialForm
# from typing_extensions import ParamSpecKwargs
from django.db.models.query import InstanceCheckMeta
from django.forms.models import ALL_FIELDS
from django.shortcuts import  render,redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import HttpResponse
from django import template
from .models import Person
# from .forms import *
from guest.forms import studentform
from django.contrib.auth.decorators import login_required
from members.decorators import allowed_users, admin_only
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.db.models import Q
# from django.forms.models import model_dict
# Create your views here.

@login_required(login_url='login')  
@allowed_users(allowed_roles=['student','teacher'])
def  view_searchbar(request):
     
    #  f = Person.objects.all()
    
    # city_record = City.objects.all()
    # print(request.POST)
    # # return render(request,'record.html',{'stud12':stud_record})
    #  group=None
    # #  user=None
    #  if request.user.groups.exists():
        # user = Group.objects.get(name = 'teacher' )'
       
        # user = User.objects.filter(username = request.user)
        if request.user.groups.filter(name='teacher'): 
             group = Group(name="teacher") 
            
            # return redirect('home')
        # group = Group.objects.get(id=group_id)
        # if user.groups.filter(name=group):  
        # if request.user in group
        
        # group = request.user.groups.all()[0].name
        
            
           
             return render(request,'record.html',{'group':group})

        else :
            return render(request,'record.html',{})
     
    # return render(request, "record.html")
# def home(request):
#     # return HttpResponse("hello")
#     return render(request,'home.html')
@login_required(login_url='userpage') 
@allowed_users(allowed_roles=['teacher'])
def search_venue(request):
       
    
    # form= Person.objects.all()
    
    
    
    #   return redirect ('search_')
        
       
       
    # else:
    #        return render(request,'search_venues.html',{})


# def detail_view(request, id):
# 	# dictionary for initial data with
# 	# field names as keys
# 	context ={}

# 	# add the dictionary during initialization
# 	context["data"] = Person.objects.get(id = id)
		
# 	return render(request, "detail_view.html", context)
    
# def update_view(request,id):

# #  form= Person.objects.get(pk=Person_reg)

#     context ={}
 
#     # fetch the object related to passed id
#     obj = get_object_or_404(Person, id = id)
 
#     # pass the object as instance in form
#     form = studentform(request.POST or None, instance = obj)
 
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         # return HttpResponseRedirect("/"+id)
 
#     # add form dictionary to context
#     context["form"] = form
 
#     return render(request, "update_venue.html", context)
        stu = Person.objects.all()
        paginator = Paginator(stu, 8)
        page = request.GET.get('page')
        try:
            studs = paginator.get_page(page)
        except PageNotAnInteger:
            studs = paginator.page(1)
        except EmptyPage:
            studs = paginator.page(paginator.num_pages)

        context = {'stu':stu, 'studs':studs}
        # context["dataset"] = Person.objects.all()
        return render(request,'search_venue.html',context)


def viewperson(request):
    global searched
    
    if request.method =="POST":
        searched = request.POST ['searched']
        # venues = Person.objects.filter(name__contains = searched)
        person_list=Person.objects.filter( reg =searched )
        
        return render(request,'person_list.html',{"searched":searched,"person_list":person_list})
        # return render(request,'search_venues.html',{"searched":searched})   
    else:
        return render(request,'record.html',{})
    
def delete_venue(request,reg):
   
    
    form =Person.objects.all().get(reg=reg)
   
    form.delete()
    messages.success(request, 'Deleted successfuly')
    return redirect ('search-venues')
    # return render (request,'record.html',{} )


# def search_venue(request):
#     global test
#     if test==Person.reg:
#       form= Person.objects.all().order_by('-reg')
#       return render(request,'search_venue.html',{"form":form})
#     else:
#     #   return redirect ('search_')
#        form= Person.objects.all().order_by('-reg')
#        return render(request,'search_venue.html',{"form":form})


def update_venue(request):    #for updating
    # rson_list=Person.objects.all()
    context ={}
    # form= studentform()
    # if request.method =="POST":
    form = studentform(request.POST or None)
    if form.is_valid():
       form.save()
       messages.success(request, 'Created successfully.')
       return redirect ('search-venues')
    context["form"] = form
        
    return render(request, "update_venue.html", context)
    
    # return render(request,'update_venue.html',{'form':form})
      


def edit_venue(request,id):  #for editing
    
    
    
    #  form =Person.objects.get(id=id)
     obj = get_object_or_404(Person, id = id)
     form = studentform(request.POST or None,instance=obj)
    
    
    
    
     if form.is_valid():
            form.save()
            messages.success(request, 'updated successfully.')
            return redirect ('search-venues')
    # else:
    #    form =Person.objects.all()
    #    form = studentform(request.POST or None,request.FILES)
     return render(request,'edit_venue.html',{'form':form,'form':form,})
    


   
    
    
    #    else :
    #      pi= Person.objects.get(pk=Person_reg)  
       
    #      fm = venueForm(instance=Person_reg) 
    #      fm= venueForm()
    # return redirect ('search-venues')
    # return render(request,'update_venue.html',{'form':form,'form':form})
      