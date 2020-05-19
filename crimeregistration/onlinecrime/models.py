from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy


CHOICES = (
		("1", "User"),
		("2", "Employee")
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