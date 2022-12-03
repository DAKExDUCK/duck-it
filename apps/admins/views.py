from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.shortcuts import render, redirect


@login_required(login_url='login')
def admin(request: HttpRequest):
    if not request.user.is_staff:
        redirect('home')
    
    return redirect('/admins/panel')