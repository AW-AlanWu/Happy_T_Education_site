from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course

@login_required(login_url="personal:login")
def course(request):
    Course.objects.order_by('-pk')
    context = {
        'Courses_List' : Course.objects.order_by('-pk')
    }
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'course/course.html', context=context)

@login_required(login_url="personal:login")
def problem(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'course/problem.html', context=context)

@login_required(login_url="personal:login")
def new(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'course/new.html', context=context)

@login_required(login_url="personal:login")
def detail(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'course/detail.html', context=context)

@login_required(login_url="personal:login")
def check(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'course/check.html', context=context)