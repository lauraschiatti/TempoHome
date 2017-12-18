from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'usersprofiles/home.html')

def authentication(request): #sign up & login with the same method
    if request.method == 'POST':
        # Post data
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        #debemos diferenciar si es el form de login o el de sign up usando el atributo
        #action definido en el HTML form
        action = request.POST.get('action', None) #valor de action que venga en el POST DE MI REQUEST

        if action == "signup":
            user = User.objects.create_user(username=username, password=password) #crear un usuario
            user.save()
        elif action == "login":
            user = authenticate(username=username, password=password) #validar que el username y password coincida con algun usuario registrado
            login(request, user)
        return redirect('/')

    return render(request, 'login.html', {})
