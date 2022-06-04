"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import request
from django.urls import path

from guest.views import view_searchbar
from guest import views
# from guest.views import search_venues
from guest.views import viewperson
from guest.views import update_venue
# from guest.views import edit_venue
from guest.views import search_venue
from members.views import registerpage
from members.views import registerpagestudent
from members.views import loginPage,logoutUser,logoutUserr,userpage
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth import views as auth_views   #auth_views
from guest import views
# 


from django.conf.urls import include, url





#   https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html    REPORTS GEN
urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    url(r'^record1/', view_searchbar,name='home'),
    # path('',include('guest.urls')),
    # path(search_venues, name='search-venue')
    url(r'^direct/', search_venue,name='search-venues') ,  
    #  path('search_venues/', views.search_venues(request), name='search_venue'),        
    url(r'^result/', viewperson,name='view_persons') ,                                         
    url(r'^create/', update_venue,name='update_venues') ,
    # url(r'^delete/<reg>', delete_venue,name='delete_venues') 
    path('delete/<reg>',views.delete_venue,name='delete_venue' ),
    path('edit/<id>',views.edit_venue,name='edit_venue' ),
    # path('blog/', include('django.contrib.auth.urls')),
    # path('blog/', include('members.urls')),
    path('register/',registerpage,name="register" ),
    path('register1/',registerpagestudent,name="registerstudent" ),
    path('login/', loginPage, name="login"),  
	path('logout/', logoutUser, name="logout"),
    path('logout1/', logoutUserr, name="logoutt"),
    
    path('user/',userpage,name="userpage"),


    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
     

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

    path('password/',auth_views.PasswordChangeView.as_view(template_name="changepass.html"),name="password_change"),

    path('password_change_done/', 
        auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"), 
        name="password_change_done"),

                                                 ]       
