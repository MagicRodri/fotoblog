from dataclasses import fields
from .models import Photo, Post , Comment
from django import forms

class UploadPhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image','caption']

class CreatePostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','summary','content']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']