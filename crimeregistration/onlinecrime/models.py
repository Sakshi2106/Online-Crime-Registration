from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
    	return self.signup_as


	