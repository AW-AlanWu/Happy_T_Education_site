from django.shortcuts import render
from django.http import HttpResponse

def course(request):
    return render(request, 'course/course.html')

def problem(request):
    return render(request, 'course/problem.html')
