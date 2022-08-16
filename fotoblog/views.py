
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from blog.models import Photo,Post
from itertools import chain

@login_required
def home_view(request):
    user = request.user

    posts_lookup = Q(author__in = user.follows.all()) | Q(author = user)
    posts = Post.objects.filter(posts_lookup)
    
    photos_lookups = Q(uploader__in = user.follows.all()) | Q(uploader = user)
    photos = Photo.objects.filter(photos_lookups).exclude(post__in = posts)
    
    posts_and_photos = sorted(chain(posts,photos),key=lambda instance : instance.timestamp,reverse = True)
    context = {
        'posts_and_photos' : posts_and_photos,
        'photos': photos,
        'posts' : posts
    }
    return render(request,'home.html',context = context)