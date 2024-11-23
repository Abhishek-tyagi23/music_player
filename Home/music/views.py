
from django.shortcuts import render
from django.http import HttpResponse
from . models import Card


def index(request):
    cards = Card.objects.all()
    return render(request, 'index.html', {'cards': cards})
    # for card in cards:
    #     print(card.title) 
    #     print(card.audio)
