from courses.models import Course
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from posts.models import Post
from accounts.forms import RegisterForm


def redirect_page(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('about')


def home(request: HttpRequest):
    recent_posts = Post.objects.filter(status=1).order_by('created_on').reverse()[:3]
    best_courses = Course.objects.filter(status=1).order_by('likes').reverse()[:6]

    return render(request, 'home.html', context = { 'posts': recent_posts , 'courses': best_courses })


def about(request: HttpRequest):
    recent_posts = Post.objects.filter(status=1).order_by('created_on').reverse()[:3]
    best_courses = Course.objects.filter(status=1).order_by('likes').reverse()[:6]
    
    return render(request, 'about.html', context = { 'posts': recent_posts , 'courses': best_courses })


def login_signup(request):
    start = ''
    if request.method == 'GET':
        login_form = AuthenticationForm()
        sign_up_form = RegisterForm()
    else:
        if 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            sign_up_form = RegisterForm()
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user=user)
                    return redirect('home')
        else:
            login_form = AuthenticationForm()
            sign_up_form = RegisterForm(data=request.POST)
            if sign_up_form.is_valid():
                user = sign_up_form.save()
                login(request, user=user)
                return redirect('home')
            start = 'right-panel-active'

    return render(request, 'registration/login.html', {
        'login_form': login_form,
        'sign_up_form': sign_up_form,
        'start': start
    })