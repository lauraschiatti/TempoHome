from django.forms import ModelForm, TextInput, Select, Textarea, FileInput

from .models import Room, Picture, Request

class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = ["user"]
        widgets = {
            'address': TextInput(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'description': Textarea(attrs={'class': 'form-control form-control-danger', 'rows': 3, 'required': True}),
            'rules': Textarea(attrs={'class': 'form-control form-control-danger', 'rows': 3}),
        }

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ["picture"]
        widgets = {
            'picture': FileInput(attrs={'class': 'form-control form-control-danger', 'accept': 'image/*', 'required': True}),
        }

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['status', 'comments']
        widgets = {
            'status': Select(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'comments': Textarea(attrs={'class': 'form-control form-control-danger', 'rows': 3})
        }