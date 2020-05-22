from django.contrib import admin
from .models import SignUp, Newcase, AddCriminal, Crime
# Register your models here.
admin.site.register(SignUp)
admin.site.register(Newcase)
admin.site.register(AddCriminal)
admin.site.register(Crime)
