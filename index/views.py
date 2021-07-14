from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
        context['coin'] = request.user.coin.coin
    return render(request, 'index/index.html', context=context)
