from django.contrib.auth import authenticate, logout as logout_user, login as login_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.shortcuts import render, redirect


def redirect_page(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('about')


@login_required(login_url='login')
def home(request: HttpRequest):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def login(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'auth/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            redirect('home')
        else:
            # Return an 'invalid login' error message.
            ...


@login_required(login_url='login')
def logout(request: HttpRequest):
    logout_user(request)
    return redirect('')


def register(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'auth/sign_up.html')
    elif request.method == 'POST':
        username = 'dake_duck'
        mail = 'arsengabdulin228@gmail.com'
        passwd = '123qwe123qwe'
        user = User.objects.create_user(username, mail, passwd)
        user.save()