from django import forms
from .models import Photo, Vision


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file',)


class VisionUpdateForm(forms.ModelForm):
    class Meta:
        model = Vision
        fields = ['image', 'title', 'content']

