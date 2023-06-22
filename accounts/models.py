from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

from .utils import set_profile_edit_permission, set_user_group


# Create your models here.
class User(AbstractUser):
    USER_PICTURES_PATH = 'users'
    DEFAULT_PICTURE= 'users/default.jpg'


    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = [
        (CREATOR, "Creator"),
        (SUBSCRIBER, "Subscriber")
    ]
    picture = models.ImageField(upload_to = USER_PICTURES_PATH,default = DEFAULT_PICTURE,blank = True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default = SUBSCRIBER)
    description = models.TextField(default='Empty description')
    location = models.CharField(max_length=128, default='Location not provided')
    website = models.URLField(blank=True)
    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role':CREATOR},
        symmetrical=False
    )


    def add_follow(self,user):
        qs = self.follows.filter(username = user.username)
        if not qs.exists():
            self.follows.add(user)
            
    def remove_follow(self,user):
        qs = self.follows.filter(username = user.username)
        if qs.exists():
            self.follows.remove(user)

    def __str__(self):

        return self.username

    def save(self,*args,**kargs):

        super().save(*args,**kargs)
        # On creation assign user to the appropriate group
        set_user_group(self)


    def get_absolute_url(self):
        return reverse("profile-view",kwargs={'username':self.username})
       

def user_post_save(instance,sender,created,*args, **kwargs):
    
    if created:
        set_profile_edit_permission(instance)

post_save.connect(user_post_save,sender=User)