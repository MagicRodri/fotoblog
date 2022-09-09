from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import pre_save,post_save

from .utils import (
    slugify_instance_title,
    set_words_count,
    set_post_change_and_delete_permission,
    set_photo_change_and_delete_permission
    )

from PIL import Image
from django_quill.fields import QuillField
# Create your models here.
User = get_user_model()

class Photo(models.Model):

    IMG_MAX_SIZE = (800,800)

    image = models.ImageField(upload_to = 'photos')
    caption = models.CharField(max_length=128,blank=True,null=True)
    uploader = models.ForeignKey(User,on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)

    def resize_image(self):
        image = Image.open(self.image)

        image.thumbnail(self.IMG_MAX_SIZE)
        image.save(self.image.path)

    def save(self,*args,**kargs):

        if self.image:
            self.resize_image()
        super().save(*args,**kargs)
        

class Post(models.Model):

    photo = models.ForeignKey(Photo,null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=128)
    summary = models.TextField(blank=True)
    slug = models.SlugField(max_length=128, unique=True,blank=True,null=True)
    content = QuillField(blank=True)
    words_count = models.IntegerField(blank=True ,null=True )
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail-view", kwargs={"slug": self.slug})

    def save(self,*args,**kargs):

        super().save(*args,**kargs)
    
def post_pre_save(sender,instance,*args,**kargs):
    set_words_count(instance)
    if instance.slug is None:
        slugify_instance_title(instance,save=False)

pre_save.connect(post_pre_save,sender=Post)

def post_post_save(sender,instance,created,*args,**kargs):
    set_post_change_and_delete_permission(instance)
    if created :
        slugify_instance_title(instance,save=True)

post_save.connect(post_post_save,sender=Post)


def  photo_post_save(sender,instance,created,*args, **kwargs):
    set_photo_change_and_delete_permission(instance)


post_save.connect(photo_post_save,sender=Photo)