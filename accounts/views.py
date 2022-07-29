from django.contrib.auth import login
from django.shortcuts import render
from .forms import LoginForm


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

        else:
            message = "Login failed"
            
    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'login.html',context = context)