from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from datetime import date
from django.db.models import Q

from .models import Room, Picture, Request
from .forms import RoomForm, PictureForm, RequestForm

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

# global variables
q = ''
room_list = ''
def search(request):
   # check that 'q' exists in request.GET
   if 'q' in request.GET:
       global q # modify global copy of q
       q = request.GET.get('q')
       # get available rooms whose address contains q, without being case-sensitive.
       global room_list # modify global copy of room_list
       room_list = Room.objects.filter(address__icontains=q).exclude(user=request.user)
   else:
       global room_list  # modify global copy of room_list
       room_list = Room.objects.all()

   return render(request, 'accommodation/search_results.html', {'room_list': room_list, 'q': q})

def post_request(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # room info
        room_id = request.POST.get('room')
        room = Room.objects.get(pk=room_id)

        # parse dates to required format for fields DateField typed
        daterange = request.POST.get('daterange')
        start_date, end_date = daterange.split("-")

        start_date = start_date.replace('/', '-')
        year, month, day = start_date.split("-")
        start_date = date(int(year), int(month), int(day))

        end_date = end_date.replace('/', '-')
        year, month, day = end_date.split("-")
        end_date = date(int(year), int(month), int(day))

        # save new request
        new_request = Request(start_date=start_date, end_date=end_date, user=request.user, room=room)
        new_request.save()

        message = "Your request sent successfully. Room's owner will get in touch with you as soon as possible"
        return render(request, 'accommodation/search_results.html', {'room_list': room_list, 'q': q, 'message': message, 'request': new_request})

class RequestList(ListView):
   model = Request

   def get_queryset(self):
       user_requests = Request.objects.filter(room__user=self.request.user)
       return user_requests

class RequestUpdate(UpdateView):
   model = Request
   success_url = reverse_lazy('accommodation:requests_list')
   form_class = RequestForm

def responses_list(request):
   user_responses = Request.objects.filter(user=request.user)

   return render(request, 'accommodation/response_list.html', {'responses': user_responses})
