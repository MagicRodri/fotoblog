import random
from django.utils.text import slugify
from guardian.models import UserObjectPermission

def slugify_instance_title(instance,save=False,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__    
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists() :
        rand_int= random.randint(1,400_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_title(instance,save=save,new_slug=slug)
    instance.slug = slug
    if save : 
        instance.save()
    return instance

def set_post_change_and_delete_permission(post=None):
    # Give post's author change and delete permissions 
    if post is not None:
        if not post.author.has_perm('change_post', post):
            UserObjectPermission.objects.assign_perm('change_post', post.author, obj=post)
        if not post.author.has_perm('delete_post', post):
            UserObjectPermission.objects.assign_perm('delete_post', post.author, obj=post)

def set_photo_change_and_delete_permission(photo=None):
    #Give photo's uploader change and delete permissions
    if photo is not None:
        if not photo.uploader.has_perm('change_photo', photo):
            UserObjectPermission.objects.assign_perm('change_photo', photo.uploader, obj=photo)
        if not photo.uploader.has_perm('delete_photo', photo):
            UserObjectPermission.objects.assign_perm('delete_photo', photo.uploader, obj=photo)
