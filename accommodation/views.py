from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from datetime import date

from .models import Room, Picture, Request
from .forms import RoomForm, PictureForm

def dashboard(request):
    return render(request, 'accommodation/dashboard.html')

def create_room(request):
    # formsets allow the user to store several pictures at once
    PicureFormSet = modelformset_factory(Picture, form=PictureForm)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        room_form = RoomForm(request.POST)
        picture_formset = PicureFormSet(request.POST, request.FILES, queryset=Picture.objects.none())

        # check whether it's valid
        if room_form.is_valid() and picture_formset.is_valid():
            new_room = room_form.save(commit=False)
            new_room.user = request.user
            new_room.save()

            for form in picture_formset.cleaned_data:
                picture = Picture(picture=form['picture'], room=new_room)
                picture.save()

            return HttpResponseRedirect('/account/rooms')

    # return blank forms
    else:
        room_form = RoomForm()
        picture_formset = PicureFormSet(queryset=Picture.objects.none())

    return render(request, 'accommodation/room_form.html', {'room_form': room_form, 'picture_formset': picture_formset})

class RoomList(ListView):
   model = Room

   def get_queryset(self):
       user_rooms = Room.objects.filter(user=self.request.user)
       return user_rooms

class RoomDetail(DetailView):
   model = Room

class RoomDelete(DeleteView):
   model = Room
   success_url = reverse_lazy('accommodation:rooms_list')

def search(request):
   # check that 'q' exists in request.GET
   if 'q' in request.GET:
       q = request.GET.get('q')

       # Get available rooms whose address contains q, without being case-sensitive.
       room_list = Room.objects.filter(address__icontains=q)
   else:
       room_list = Room.objects.all()

   return render(request, 'accommodation/search_results.html', {'room_list': room_list, 'q': q})










