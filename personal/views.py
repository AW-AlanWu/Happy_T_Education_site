from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url="personal:login")
def userProfile(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
        context['coin'] = request.user.coin.coin
    return render(request, 'personal/userProfile.html', context=context)

def register(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
        context['coin'] = request.user.coin.coin
    return render(request, 'personal/register.html', context=context)

def login(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'personal/login.html', context=context)

def saveAccount(request):
    if User.objects.filter(username = request.POST['username']) or User.objects.filter(email = request.POST['email']):
        raise Http404("username or email already exists")
    else:
        user = User.objects.create_user(
            request.POST['username'],
            request.POST['email'],
            request.POST['password'],
        )
        user.save()
        c = Coin(user=user)
        c.save()
        if request.POST['options'] == 'teacher':
            t = Teacher(user=user)
            t.save()
        elif request.POST['options'] == 'student':
            s = Student(user=user)
            s.save()
        return HttpResponseRedirect(reverse('personal:login'))

def authenticateAccount(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect(reverse('index:index'))
    else:
        raise Http404("The account does not exist")

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('personal:login'))