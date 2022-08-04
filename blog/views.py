
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UploadPhotoForm, CreatePostForm
from .models import Photo,Post
# Create your views here.

@login_required
def upload_photo_view(request):

    form = UploadPhotoForm()
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST,request.FILES)

        if form.is_valid():
            photo=form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect(reverse('home-view'))

    return render(request,'blog/upload_photo.html',context={'form':form})

@login_required
def create_post_view(request):
    user = request.user
    photo_form = UploadPhotoForm()
    post_form = CreatePostForm()
    if request.method == 'POST':
        photo_form = UploadPhotoForm(request.POST,request.FILES)
        post_form = CreatePostForm(request.POST)
        if all([photo_form.is_valid(),post_form.is_valid()]):
            photo =  photo_form.save(commit=False) # retrieve the photo without pushing into the db
            photo.uploader = user # Set the uploader
            photo.save() # Push to the db

            # Same procedure for the post instance
            post = post_form.save(commit=False)
            post.photo = photo
            post.author = user
            post.save()

            return redirect(reverse('home-view'))

    context = {
        'photo_form':photo_form,
        'post_form':post_form
    }
    return render(request,'blog/create_post.html',context=context)

def post_detail_view(request,slug=None):
    post = None
    if slug is not None:
        post = get_object_or_404(Post,slug=slug)

    return render(request,'blog/post_detail.html',context={'post':post})
