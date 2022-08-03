from dataclasses import fields
from .models import Photo, Post
from django import forms

class UploadPhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image','caption']

class CreatePostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','content']