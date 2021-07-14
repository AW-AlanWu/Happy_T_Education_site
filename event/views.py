from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="personal:login")
def event(request):
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    return render(request, 'event/event.html', context=context)
