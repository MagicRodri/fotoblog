from multiprocessing import context
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import UploadPhotoForm
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
