from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import User
from .models import Bet
from .models import Response

def api_response(success, payload):
    return JsonResponse({'success': success, 'data': payload})

@csrf_exempt
def user_Create_GetAll(request):
    if request.method == 'POST':
        user = User(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            username=request.POST["username"],
            password=request.POST["password"],
            num_tokens=request.POST["num_tokens"],
            num_flags=request.POST["num_flags"]
        )
        try:
            user.save()
        except:
            return api_response(False, 'Could not create user')
        return api_response(True, 'User successfully inserted into database')
    elif request.method == 'GET':
        users = User.objects.all()
        data = [ obj.as_json() for obj in users ]
        return api_response(True, data)
    else:
        return api_response(False, "Unable to process HTTP Request")        

@csrf_exempt
def bet_Create_GetAll(request):
    if request.method == 'POST':
        bet = Bet(
            privacy=request.POST["privacy"],
            response_limit=request.POST["response_limit"],
            question=request.POST["question"],
            description=request.POST["description"],
            min_buyin=request.POST["min_buyin"],
            per_person_cap=request.POST["per_person_cap"]
        )
        try:
            bet.save()
        except:
            return api_response(False, 'Could not create bet')
        return api_response(True, 'Bet successfully inserted into database')
    elif request.method == 'GET':
        bets = Bet.objects.all()
        data = [ obj.as_json() for obj in bets ]
        return api_response(True, data)
    else:
        return api_response(False, "Unable to process HTTP Request")

@csrf_exempt
def response_Create_GetAll(request):
    if request.method == 'POST':
        response = Response(
            user_id=request.POST["user_id"],
            bet_id=request.POST["bet_id"],
            answer=request.POST["answer"],
            amount=request.POST["amount"]
        )
        try:
            response.save()
        except:
            return api_response(False, 'Could not create response')
        return api_response(True, 'Response successfully inserted into database')
    elif request.method == 'GET':
        responses = User.objects.all()
        data = [ obj.as_json() for obj in responses ]
        return api_response(True, data)
    else:
        return api_response(False, "Unable to process HTTP Request")

@csrf_exempt
def user_get_update_delete(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return api_response(False, 'User not found')
    
    if request.method == 'GET':
        data = user.as_json()
        return api_response(True, data)
    elif request.method == 'POST':
        for key,value in request.POST.items():
            setattr(user, key, value)
        user.save()
        return api_response(True, 'Updated User field(s)')
    elif request.method == 'DELETE':
        user.delete()
        return api_response(True, 'User '+user_id+' deleted')
    else:
        return api_response(False, "Unable to process HTTP Request")

@csrf_exempt
def bet_get_update_delete(request, bet_id):
    try:
        bet = Bet.objects.get(pk=bet_id)
    except Bet.DoesNotExist:
        return api_response(False, 'Bet not found')
    
    if request.method == 'GET':
        data = bet.as_json()
        return api_response(True, data)
    elif request.method == 'POST':
        for key,value in request.POST.items():
            setattr(bet, key, value)
        bet.save()
        return api_response(True, 'Updated Bet field(s)')
    elif request.method == 'DELETE':
        bet.delete()
        return api_response(True, 'Bet '+bet_id+' deleted')
    else:
        return api_response(False, "Unable to process HTTP Request")

@csrf_exempt
def response_get_update_delete(request, response_id):
    try:
        response = Response.objects.get(pk=response_id)
    except Response.DoesNotExist:
        return api_response(False, 'Response not found')
    
    if request.method == 'GET':
        data = response.as_json()
        return api_response(True, data)
    elif request.method == 'POST':
        for key,value in request.POST.items():
            setattr(response, key, value)
        response.save()
        return api_response(True, 'Updated Response field(s)')
    elif request.method == 'DELETE':
        response.delete()
        return api_response(True, 'Response '+response_id+' deleted')
    else:
        return api_response(False, "Unable to process HTTP Request")

# def getResponsesForBet(request, bet_id):
#     try:
#         bet = Bet.objects.get(pk=bet_id)
#     except Bet.DoesNotExist:
#         return api_response(False, "Bet not found")
#     responses = bet.response_set.all()
#     data = [r.as_json() for r in responses]
#     return api_response(True, data)
