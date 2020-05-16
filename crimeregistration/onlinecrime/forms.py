from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import SignUp

		

class SignUpForm(forms.ModelForm):
     
	
	class  Meta:
		model = SignUp
		fields =  ( 'email', 'signup_as',)



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']