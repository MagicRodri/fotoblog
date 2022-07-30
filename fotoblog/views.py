
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from blog.models import Photo

@login_required
def home_view(request):
    photos = Photo.objects.all()
    context = {

        'photos': photos
    }
    return render(request,'home.html',context = context)