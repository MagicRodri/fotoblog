
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from .forms import LoginForm, SignUpForm,PpUploadForm, EditProfileForm
from django.urls import reverse
from blog.models import Photo,Post
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def login_view(request):

    form = LoginForm(request)
    message = ""
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect(reverse('home-view'))

        else:
            message = "Login failed"
            
    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'accounts/login.html',context = context)


def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect(reverse('login-view'))

    return render(request,'accounts/logout.html',context={})


def signup_view(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect(reverse('home-view'))

    return render(request,'accounts/signup.html',context={'form':form})


def profile_view(request):
    user = request.user
    photos = Photo.objects.filter(uploader=user)
    context = {
        'user' : user,
        'photos': photos
    }

    return render(request,'accounts/profile.html', context=context)

def upload_pp_view(request):
    form = PpUploadForm(instance=request.user)
    if request.method == 'POST':
        form = PpUploadForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile-view'))
    context = {
        'form' : form
    }
    return render(request,'accounts/upload_profile_picture.html',context=context)

def edit_profile_view(request):
    user = request.user
    form = EditProfileForm(instance=user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile-view'))
    context = {
        'form' : form
    }

    return render(request,'accounts/edit_profile.html',context=context)

def delete_profile_view(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        return redirect(reverse('login-view'))

    return render(request,'accounts/delete_profile.html',context={})