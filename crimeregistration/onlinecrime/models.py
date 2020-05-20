from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy


CHOICES = (
		("1", "User"),
		("2", "Employee")
		)

GENDER = (
		("1", "Male"),
		("2", "Female"),
		("3", "Other")
		)

class SignUp(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    signup_as = models.CharField(max_length=1, choices = CHOICES, default = "User")
    email = models.EmailField(blank=True )
    def save(self, *args, **kwargs):
    	super().save(*args, **kwargs)


class Newcase(models.Model):
	#user = models.ForeignKey(User, on_delete = models.CASCADE)
	case_title = models.CharField(max_length = 50)
	date = models.DateField()
	description = models.TextField()
	case_status = models.CharField(max_length = 50, default = "pending")
	username = models.CharField(max_length = 20)
	
	
    

	def __str__(self):
		return  self.case_title


class AddCriminal(models.Model):
	criminal_name = models.CharField(max_length = 50)
	address = models.CharField(max_length = 250)
	city = models.CharField(max_length = 20)
	state = models.CharField(max_length = 20)
	country = models.CharField(max_length = 20)
	email = models.EmailField(blank = True)
	mobile = models.IntegerField()
	gender = models.CharField(max_length = 1, choices = GENDER, default = "Male")
	dob = models.DateField()
	photo = models.FileField()
	description = models.TextField()

	def __str__(self):
		return self.criminal_name