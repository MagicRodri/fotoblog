from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Photo(models.Model):

    image = models.ImageField(upload_to = 'photos')
    caption = models.CharField(max_length=128,blank=True,null=True)
    uploader = models.ForeignKey(User,on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)


class Post(models.Model):

    photo = models.ForeignKey(Photo,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    content = models.TextField(blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)