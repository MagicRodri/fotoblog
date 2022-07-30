from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from pathlib import Path
from django.core.files import File
from django.conf import settings
from django.db.models.signals import pre_save

# Create your models here.
class User(AbstractUser):
    USER_PICTURES_PATH = 'users'
    DEFAULT_PICTURE= USER_PICTURES_PATH +  '/' + 'default.jpg'


    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = [
        (CREATOR, "Creator"),
        (SUBSCRIBER, "Subscriber")
    ]
    picture = models.ImageField(upload_to = USER_PICTURES_PATH,blank = True, null = True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    def __str__(self):

        return self.username

    def get_absolute_url(self):
        return reverse("profile-view")




def set_default_picture(sender,instance,*args,**kargs):
    if instance.picture is None:
        instance.picture = instance.DEFAULT_PICTURE

pre_save.connect(set_default_picture,sender=User)           