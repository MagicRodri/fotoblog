
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from blog.models import Photo,Post

@login_required
def home_view(request):
    photos = Photo.objects.all()
    posts = Post.objects.all()
    context = {

        'photos': photos,
        'posts' : posts
    }
    return render(request,'home.html',context = context)