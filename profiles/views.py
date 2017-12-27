from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .forms import *

def home(request):
    return render(request, 'profiles/home.html')

def sign_up(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        # check whether it's valid
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new instance from the form's data
            new_user = user_form.save()
            # Form brings back a plain text string, not an encrypted password
            pw = new_user.password
            # Thus we need to use set password to encrypt the password string
            new_user.set_password(pw)
            # Save the new instance
            new_user.save()

            # Create, but don't save the new profile instance
            new_profile = profile_form.save(commit=False)
            # Set user field
            new_profile.user = new_user
            # Save new profile
            new_profile.save()

            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            # redirect to a new URL:
            return HttpResponseRedirect('/accommodation/dashboard')

    # if a GET (or any other method) we'll create a blank form
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'profiles/sign_up.html', {'user_form': user_form, 'profile_form': profile_form})

def authentication(request):
    # redirect back if authenticated
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        # post data
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        # check if credentials match with a registered user
        user = authenticate(username=username, password=password)
        if user is not None:
            # correct username and password, so login the user
            login(request, user)
            # redirect to a success page
            return HttpResponseRedirect('/')
        else:
            # return an 'invalid login' error message
            message = 'Username and password were incorrect.'
            return render(request, 'profiles/login.html', {'message': message})

    return render(request, 'profiles/login.html', {})