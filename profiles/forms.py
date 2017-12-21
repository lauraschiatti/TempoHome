from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, FileInput, Select, Textarea

from .models import Profile
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]
        widgets = {
            'username': TextInput(attrs={'class': 'form-control form-control-danger'}),
            'email': EmailInput(attrs={'class': 'form-control form-control-danger'}),
            'password': PasswordInput(attrs={'class': 'form-control form-control-danger'}),
            'first_name': TextInput(attrs={'class': 'form-control form-control-danger'}),
            'last_name': TextInput(attrs={'class': 'form-control form-control-danger'}),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        widgets = {
            'gender': Select(attrs={'class': 'form-control form-control-danger'}),
            'nationality': TextInput(attrs={'class': 'form-control form-control-danger'}),
            'passport_number': TextInput(attrs={'class': 'form-control form-control-danger'}),
            'passport_file': FileInput(attrs={'class': 'form-control form-control-danger', 'accept':'application/pdf'}),
            'phone_number': TextInput(attrs={'class': 'form-control form-control-danger', 'accept': 'image/*'}),
            'picture': FileInput(attrs={'class': 'form-control form-control-danger'}),
            'role': Select(attrs={'class': 'form-control form-control-danger'}),
            'description': Textarea(attrs={'class': 'form-control form-control-danger', 'placeholder': 'Let us know your spoken languages, hobbies and related stuff about you', 'rows': 5}),
        }