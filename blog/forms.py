from .models import Photo, Post
from django import forms

class UploadPhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image','caption']