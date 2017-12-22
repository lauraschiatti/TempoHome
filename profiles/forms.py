from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput, Select, Textarea

from .models import Profile
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]
        widgets = {
            'username': TextInput(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'email': EmailInput(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'password': PasswordInput(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'first_name': TextInput(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'last_name': TextInput(attrs={'class': 'form-control form-control-danger', 'required': True}),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        widgets = {
            'gender': Select(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'nationality': TextInput(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'passport_number': TextInput(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'passport_file': FileInput(attrs={'class': 'form-control form-control-danger', 'accept':'application/pdf', 'required': True}),
            'phone_number': TextInput(attrs={'class': 'form-control form-control-danger', 'accept': 'image/*', 'required': True}),
            'picture': FileInput(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'role': Select(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'description': Textarea(attrs={'class': 'form-control form-control-danger', 'placeholder': 'Let us know your spoken languages, hobbies and related stuff about you', 'rows': 5, 'required': True}),
        }