from django.forms import ModelForm, TextInput, Select, Textarea, FileInput

from .models import Room, Picture

class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = ["user"]
        widgets = {
            'address': TextInput(attrs={'class': 'form-control form-control-danger', 'required': True}),
            'description': Textarea(attrs={'class': 'form-control form-control-danger', 'rows': 3, 'required': True}),
            'rules': Textarea(attrs={'class': 'form-control form-control-danger', 'rows': 3}),
            'status': Select(attrs={'class': 'form-control form-control-danger', 'required': True}),
        }

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ["picture"]
        widgets = {
            'picture': FileInput(attrs={'class': 'form-control form-control-danger', 'accept': 'image/*', 'required': True}),
        }