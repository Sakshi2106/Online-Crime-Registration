
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import SignUpForm, AddCase, UserForm, AddCriminalForm, AddCrimeForm
from .models import SignUp, Newcase, AddCriminal, Crime
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

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
			
		return redirect('home')	

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
	
	


class EmployeeDashboardView(TemplateView):
	template_name = "onlinecrime/employee_dashboard.html"


def logout_user(request):
	logout(request)
	form = UserCreationForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, 'onlinecrime/home.html', context)

class AddCaseView(View):
	form_class = AddCase
	template_name = "onlinecrime/Newcase_form1.html"

	#display blank form
	def get(self, request):
		addcase_form = AddCase(initial={'username': request.user.username})
		return render(request, self.template_name, { 'addcase_form' : addcase_form})

	def post(self, request):
		addcase_form = AddCase(request.POST, )
		
		
		if addcase_form.is_valid():
			
			addcase = addcase_form.save(commit=False)
			addcase.save()
		return redirect('allcases')	


class AddCriminalView(View):
	form_class = AddCriminalForm
	template_name = "onlinecrime/addcriminal_form.html"

	def get(self, request):
		addcriminal_form = AddCriminalForm()
		return render(request, self.template_name, { 'addcriminal_form' : addcriminal_form})

	def post(self, request):
		addcriminal_form = AddCriminalForm(request.POST, request.FILES)
		
		
		if addcriminal_form.is_valid():
			addcriminal_form.save()
			return redirect('employeedashboard')

		else:
			return render(request, self.template_name, { 'addcriminal_form' : addcriminal_form})




	

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, "Password Changed Successfully!")
			return redirect('home')
		else:
			messages.error(request, 'Invalid')

	else:
		form = PasswordChangeForm(request.user)

	return render(request, 'onlinecrime/change_password.html', {'form':form})
		


def AllCases_OfLoggedUserView(request):
	allcases = Newcase.objects.filter(username = request.user.username)
	return render(request, "onlinecrime/allcases.html", { 'allcases' : allcases} )
		

def user_update_view(request): 
	if request.method == 'GET':
		user = request.user
		account_details = SignUp.objects.filter(user  = user).first()
		username = request.user.username
		password = request.user.password
		user_form = UserCreationForm( initial = {'username': username, 'password1': password, 'password2': password})
		signup_form = SignUpForm(request.GET or None, instance = account_details)
		#signup_form = SignUpForm( request.GET or None, instance = account_details )
		user_form.fields['password1'].widget.render_value = True
		user_form.fields['password2'].widget.render_value = True
		return render(request, 'onlinecrime/update_profile.html', {'signup_form': signup_form, 'user_form': user_form})
	else:
		user_form = UserCreationForm(request.POST)
		signup_form = SignUpForm(request.POST)

		if user_form.is_valid() and signup_form.is_valid():
			user_form.save()
			signup_form.save()

		return redirect('userdashboard')

def employee_update_view(request):
	if request.method == 'GET':
		user = request.user
		account_details = SignUp.objects.filter(user  = user).first()
		username = request.user.username
		password = request.user.password
		user_form = UserCreationForm( initial = {'username': username, 'password1': password, 'password2': password})
		signup_form = SignUpForm(request.GET or None, instance = account_details)
		#signup_form = SignUpForm( request.GET or None, instance = account_details )
		user_form.fields['password1'].widget.render_value = True
		user_form.fields['password2'].widget.render_value = True
		return render(request, 'onlinecrime/update_profile.html', {'signup_form': signup_form, 'user_form': user_form})
	else:
		user_form = UserCreationForm(request.POST)
		signup_form = SignUpForm(request.POST)

		if user_form.is_valid() and signup_form.is_valid():
			user_form.save()
			signup_form.save()

		return redirect('employeedashboard')

def case_report_view(request):
	allcases = Newcase.objects.all()
	return render(request, "onlinecrime/employee_allcases.html", { 'allcases' : allcases} )

class Case_report_delete(DeleteView):
	model = Newcase
	success_url = reverse_lazy('case_report')		


class CaseUpdate(UpdateView):
	model = Newcase
	#form_class = AddCase
	fields = ['case_title', 'date', 'case_status', 'description']
	#success_url = reverse_lazy('case_report')
	def get_initial(self):
		return { 'field1': 'case_title', 'field2': 'date', 'field3': 'case_status', 'field4': 'description' }

	def get_object(self):
		return Newcase.objects.get(pk=self.request.GET.get('pk')) 

class Criminal_Delete(DeleteView):
	model = AddCriminal
	success_url = reverse_lazy('criminalreport')

class Criminal_Update(UpdateView):
	model = AddCriminal
	fields = ['criminal_name', 'address', 'city', 'state', 'country', 'email', 'mobile', 'gender', 'dob', 'photo', 'description' ]

	def get_initial(self):
		return {'field1' :'criminal_name', 'field2' :'address', 'field3' :'city', 'field4' :'state', 'field5' :'country', 'field6' :'email', 'field7' :'mobile', 'field8' :'gender', 'field9' :'dob', 'field10' :'photo', 'field11' :'description' }

	def get_object(self):
		return AddCriminal.objects.get(pk=self.request.GET.get('pk'))


def update_view(request): 
    if request.method == 'GET':
	    user = request.user
	    account_details = SignUp.objects.filter(user  = user).first()
	    username = request.user.username
	    password = request.user.password
	    user_form = UserCreationForm( initial = {'username': username, 'password1': password, 'password2': password})
	    signup_form = SignUpForm(request.GET or None, instance = account_details)
	   	#signup_form = SignUpForm( request.GET or None, instance = account_details )
	    user_form.fields['password1'].widget.render_value = True
	    user_form.fields['password2'].widget.render_value = True
	    return render(request, 'onlinecrime/update_profile.html', {'signup_form': signup_form, 'user_form': user_form})


def CriminalReport(request):
	criminalreport = AddCriminal.objects.all()
	return render(request, 'onlinecrime/criminalreport.html', {'criminalreport' : criminalreport})


class AddCrimeView(View):
	form_class = AddCrimeForm
	template_name = "onlinecrime/addcrime_form.html"

	def get(self, request):
		addcrime_form = AddCrimeForm()
		return render(request, self.template_name, { 'addcrime_form' : addcrime_form})

	def post(self, request):
		addcrime_form = AddCrimeForm(request.POST)
		
		
		if addcrime_form.is_valid():
			addcrime_form.save()
			return redirect('employeedashboard')

		else:
			return render(request, self.template_name, { 'addcrime_form' : addcrime_form})


def CrimeReport(request):
	crimereport = Crime.objects.all()
	return render(request, 'onlinecrime/crimereport.html', {'crimereport' : crimereport})

class Crime_Delete(DeleteView):
	model = Crime
	success_url = reverse_lazy('crimereport')

class Crime_Update(UpdateView):
	model = Crime
	fields = ['criminal_name', 'crime_title', 'crime_date', 'crime_description']

	def get_initial(self):
		return {'field1' :'criminal_name', 'field2' :'crime_title', 'field3' :'crime_date', 'field4' :'crime_description'}

	def get_object(self):
		return Crime.objects.get(pk=self.request.GET.get('pk'))
