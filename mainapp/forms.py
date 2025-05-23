from django import forms
from django.contrib.auth.models import User
from .models import AudioFile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']


class AudioUploadForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['audio']
