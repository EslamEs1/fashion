from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import CustomUser


def login(request):
    context = {}
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
            else:
                messages.error(request, 'Invalid username or password')
        except CustomUser.DoesNotExist:
            return redirect('/api/login/')

    return render(request, 'account/login.html', context)



@login_required
def logout_view(request):
    logout(request)

@login_required
def signup(request):
    return render(request, 'account/register.html', {})
