from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import pre_save,post_save
from .utils import slugify_instance_title
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
    slug = models.SlugField(max_length=128, unique=True,blank=True,null=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail-view", kwargs={"pk": self.pk})

    def save(self,*args,**kargs):

        super().save(*args,**kargs)
    
def post_pre_save(sender,instance,*args,**kargs):
    if instance.slug is None:
        slugify_instance_title(instance,save=False)

pre_save.connect(post_pre_save,sender=Post)

def post_post_save(sender,instance,created,*args,**kargs):

    if created :
        slugify_instance_title(instance,save=True)

post_save.connect(post_post_save,sender=Post)