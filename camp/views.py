from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="personal:login")
def List(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'camp/list.html', context=context)

@login_required(login_url="personal:login")
def Detail(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'camp/detail.html', context=context)

@login_required(login_url="personal:login")
def new(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'camp/new.html', context=context)

@login_required(login_url="personal:login")
def join(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'camp/join.html', context=context)