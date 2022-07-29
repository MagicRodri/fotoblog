from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):

    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = [
        (CREATOR, "Creator"),
        (SUBSCRIBER, "Subscriber")
    ]
    picture = models.ImageField(upload_to = '',blank = True, null = True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)

    def __str__(self):

        return self.username