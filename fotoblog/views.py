
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from blog.models import Photo,Post
from itertools import chain

def home_view(request):

    return render(request,'home.html')