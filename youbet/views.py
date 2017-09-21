from django.shortcuts import render
from django.http import HttpResponse, Http404
import json

from .models import User
from .models import Bet
from .models import Response

# CREATE
def createUser(request)

# READ
def getUser(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    data = json.dumps(user.as_json())
    return HttpResponse(data, content_type='application/json')

def getBet(request, bet_id):
    try:
        bet = Bet.objects.get(pk=bet_id)
    except Bet.DoesNotExist:
        raise Http404("Responses do not exist")
    data = json.dumps(response.as_json())
    return HttpResponse(data, content_type='application/json')

def getResponsesForBet(request, bet_id):
    try:
        bet = Bet.objects.get(pk=bet_id)
    except Bet.DoesNotExist:
        raise Http404("Bet does not exist")
    responses = bet.response_set.all()        
    data = json.dumps([r.as_json() for r in responses])
    return HttpResponse(data, content_type='application/json')

def getAllBets(request):
    bets = Bet.objects.all()
    data = json.dumps(bets)
    return HttpResponse(data, content_type='application/json')

# UPDATE

# DELETE