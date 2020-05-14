#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Album
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
#from django.http import Http404
#from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

"""def home(request):
	all_albums = Album.objects.all()
	context = {
		'all_albums' : all_albums
	}
	return render (request, "music/home.html" , context)

def detail(request, album_id):
	album = get_object_or_404(Album, id = album_id)
	return render(request, "music/details.html", { 'album' : album} )
		
def favourite(request, album_id):
	album = get_object_or_404(Album, id = album_id)

	try:
		selected_song = album.song_set.get(id = request.POST['song'])
		
		
	except(KeyError, Song.DoesNotExist):
		return render(request, "music/details.html", {
		 'album' : album,
		 'errormessage' : "You did not select a valid song",
		 } )
	else:
		selected_song.is_favourite = True
		selected_song.save()
		return render(request, "music/details.html", { 'album' : album} )"""

class HomeView(generic.ListView):
	template_name = "music/home.html"
	context_object_name  =  "all_albums"

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = "music/details.html"
	
class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('home')

class UserFormView(View):
	form_class = UserForm
	template_name = "music/registration_form.html"

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)
			#cleaned (normalised ) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()


			#returns  User objects if credentials are correct
			user = authenticate(username = username,password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('home')

		return render(request, self.template_name, {'form': form})
