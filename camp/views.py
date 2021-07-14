from django.shortcuts import render
from django.http import HttpResponse

def List(request):
    return render(request, 'camp/list.html')

def Detail(request):
    return render(request, 'camp/detail.html')