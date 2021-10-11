from django import forms
from django.forms import ModelForm, TextInput, FileInput, Textarea, HiddenInput

from uploadapp.models import Upload


class UploadCreationForm(ModelForm):

    class Meta:
        model = Upload
        fields = ['name', 'phone_number', 'image', 'location']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control p-1",
                'style': "",
                'placeholder': "name"
            }),
            'phone_number': TextInput(attrs={
                'class': "form-control p-1",
                'style': "",
                'placeholder': "010-0000-0000 형식으로 기입해주세요"
            }),
            'image': FileInput(attrs={
                'class': "form-control p-1",
                'style': "",
                'placeholder': "file"
            }),
            'location': HiddenInput(attrs={
                'class': "form-control p-1",
                'id': 'geolocation',
                'style': "",
                'placeholder': "위치"
            }),
        }


class UploadupdateForm(ModelForm):

    class Meta:
        model = Upload
        fields = ['name', 'phone_number', 'image', 'location']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control p-1",
                'style': "",
                'placeholder': "name"
            }),
            'phone_number': TextInput(attrs={
                'class': "form-control p-1",
                'style': "",
                'placeholder': "010-0000-0000 형식으로 기입해주세요"
            }),
            'image': FileInput(attrs={
                'class': "form-control p-1",
                'style': "",
                'placeholder': "file"
            }),
            'location': Textarea(attrs={
                'class': "form-control p-1",
                'id': 'geolocation',
                'style': "",
                'placeholder': "위치"
            }),
        }
