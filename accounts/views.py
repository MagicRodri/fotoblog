
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from .forms import LoginForm, SignUpForm
from django.urls import reverse

# Create your views here.

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