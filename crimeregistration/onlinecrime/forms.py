from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import SignUp, Newcase, AddCriminal, Crime

		

class SignUpForm(forms.ModelForm):
     
	
	class  Meta:
		model = SignUp
		fields =  ( 'email', 'signup_as',)



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

class AddCase(forms.ModelForm):
	class Meta:
		model = Newcase
		fields = ('case_title', 'date', 'description', 'username')


class AddCriminalForm(forms.ModelForm):
	class Meta:
		model = AddCriminal
		fields = ('criminal_name', 'address', 'city', 'state', 'country', 'email', 'mobile', 'gender', 'dob', 'photo', 'description' )

class AddCrimeForm(forms.ModelForm):
	class Meta:
		model = Crime
		fields = ('criminal_name', 'crime_title', 'crime_date', 'crime_description')