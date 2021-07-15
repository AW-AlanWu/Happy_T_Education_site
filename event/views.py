from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .spider import fetchEvent
from .models import Event

@login_required(login_url="personal:login")
def event(request):
    fetchEvent()
    context = {
        'event_list' : Event.objects.order_by('-pk')
    }
    if request.user.is_authenticated:
        context['is_authenticated'] = True
        context['coin'] = request.user.coin.coin
    return render(request, 'event/event.html', context=context)
