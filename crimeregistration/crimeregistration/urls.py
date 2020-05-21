"""crimeregistration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from onlinecrime.views import HomePageView, AboutPageView, SignUpFormView, UserDashboardView, AddCaseView, EmployeeDashboardView, AllCases_OfLoggedUserView, update_view, AddCriminalView
from onlinecrime import views

app_name = "onlinecrime"




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view() , name='home'),
    path('about/', AboutPageView.as_view() , name='about'),
    path('register/', SignUpFormView.as_view(), name='register'),
    path('user_login/', views.login_user, name = 'user_login'),
    path('employee_login/', views.login_employee, name = 'employee_login'),
    path('userdashboard/', UserDashboardView.as_view(), name='userdashboard'),
    path('userdashboard/addcase/' , AddCaseView.as_view(), name = 'addcase'),
    path('employeedashboard/', EmployeeDashboardView.as_view(), name='employeedashboard'),
    path('logout/', views.logout_user, name = 'logout_user'),
    path('change_password/', views.change_password, name ='change_password'),
    path('userdashboard/allcases/' , views.AllCases_OfLoggedUserView, name = 'allcases'),
    path('userdashboard/my_account/' , views.update_view, name = 'my_account'),
    path('employeedashboard/addcriminal/', AddCriminalView.as_view(), name = 'addcriminal'),

    path('employeedashboard/criminalreport/', views.CriminalReport, name = 'criminalreport')
    ]
