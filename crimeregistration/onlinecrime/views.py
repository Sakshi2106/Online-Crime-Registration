from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import SignUpForm
from .models import SignUp, Newcase
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD

from django.views.generic.edit import CreateView,UpdateView,DeleteView
=======
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
>>>>>>> 4098331cbd95006d79359f1cb4ef938fa27e6f9f

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
				
				return render(request, 'onlinecrime/user_dashboard.html', {'users': users})
			else:
				return render(request, 'onlinecrime/user_login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'onlinecrime/user_login.html', {'error_message': 'Invalid login'})
	return render(request, 'onlinecrime/user_login.html')

def login_employee(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				users = SignUp.objects.filter(user=request.user)
				
				return render(request, 'onlinecrime/employee_dashboard.html', {'users': users})
			else:
				return render(request, 'onlinecrime/employee_login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'onlinecrime/employee_login.html', {'error_message': 'Invalid login'})
	return render(request, 'onlinecrime/employee_login.html')

		#return redirect('home')

class UserDashboardView(TemplateView):
	template_name = "onlinecrime/user_dashboard.html"

<<<<<<< HEAD
class NewCaseCreate(CreateView):
	model = Newcase
	fields = ['case_title', 'date', 'description']
=======
class EmployeeDashboardView(TemplateView):
	template_name = "onlinecrime/employee_dashboard.html"


def logout_user(request):
    logout(request)
    form = UserCreationForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'onlinecrime/home.html', context)
>>>>>>> 4098331cbd95006d79359f1cb4ef938fa27e6f9f
