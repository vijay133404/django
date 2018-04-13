from django.shortcuts import render
from django.http import HttpResponse
from .models import Coin

def index(request):
    coins = Coin.objects.get(id=1)
    return render(request, 'coins/index.html', {'coins': coins})
