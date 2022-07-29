from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = [
        (CREATOR, "Creator"),
        (SUBSCRIBER, "Subscriber")
    ]
    picture = models.ImageField(upload_to = '',blank = True, null = True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)


# Create your models here.
