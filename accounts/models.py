from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from .utils import set_user_group


# Create your models here.
class User(AbstractUser):
    USER_PICTURES_PATH = 'users'
    DEFAULT_PICTURE= '/media/' + USER_PICTURES_PATH +  '/' + 'default.jpg'


    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = [
        (CREATOR, "Creator"),
        (SUBSCRIBER, "Subscriber")
    ]
    picture = models.ImageField(upload_to = USER_PICTURES_PATH,blank = True, null = True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default = SUBSCRIBER)
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
        return reverse("profile-view")
       