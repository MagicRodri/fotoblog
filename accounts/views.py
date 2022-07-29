
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from .forms import LoginForm
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
            message = f"{request.user} logged in successfully"
            return redirect(reverse('login-view'))

        else:
            message = "Login failed"
            
    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'login.html',context = context)


def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect(reverse('login-view'))

    return render(request,'logout.html',context={})