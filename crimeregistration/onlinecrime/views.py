from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import SignUpForm
from .models import SignUp
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD

from django.contrib.auth import authenticate, login
=======
from django.http import HttpResponseRedirect
>>>>>>> 0f0bd1883b35b5419e18ed49664bef16a41b1107
# Create your views here.

class HomePageView(TemplateView):

	template_name = "onlinecrime/home.html"

class AboutPageView(TemplateView):
	template_name = "onlinecrime/about.html"

class SignUpFormView(View):
	form_class = SignUpForm
	template_name = "onlinecrime/signup_form.html"

	#display blank form
	def get(self, request):
		signup_form = SignUpForm(None)
		user_form = UserCreationForm(None)
		return render(request, self.template_name, {'user_form': user_form, 'signup_form' : signup_form})

	def post(self, request):
		signup_form = SignUpForm(request.POST)
		user_form = UserCreationForm(request.POST)

		if user_form.is_valid() and signup_form.is_valid():
			user = user_form.save(commit = False)
			signup = signup_form.save(commit=False)
			
			#cleaned (normalised ) data
			
			
			user.save()

			signup.user = user
			signup.save()
			
			
<<<<<<< HEAD
		return render(request, "onlinecrime/home.html", {'user_form': user_form, 'signup_form' : signup_form})

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				users = SignUp.objects.filter(user=request.user)
				
				return render(request, 'onlinecrime/home.html', {'users': users})
			else:
				return render(request, 'onlinecrime/user_login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'onlinecrime/user_login.html', {'error_message': 'Invalid login'})
	return render(request, 'onlinecrime/user_login.html')

def login_employee(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		variable = SignUp.objects.filter(signup_as)	
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				users = SignUp.objects.filter(user=request.user)
				if variable == "User":
					return render(request, 'onlinecrime/home.html', {'users': users})
			else:
				return render(request, 'onlinecrime/employee_login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'onlinecrime/employee_login.html', {'error_message': 'Invalid login'})
	return render(request, 'onlinecrime/employee_login.html')
=======

		return redirect('home')

class UserDashboardView(TemplateView):
	template_name = "onlinecrime/user_dashboard.html"
>>>>>>> 0f0bd1883b35b5419e18ed49664bef16a41b1107
