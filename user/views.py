from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
import json
from user.models import User

@csrf_exempt
def register(request):
    if request.method == "POST":
        print(request.body)
        json_data = json.loads(request.body)
        username = json_data['username']
        password = json_data['password']
        print(json_data)
        print(username)
        print(password)
        user = User(username=username, password=password)
        user.save()
        return HttpResponse(status=201)

@csrf_exempt
def loginAttempt(request):
    print(request.body)
    json_data = json.loads(request.body)
    username = json_data['username']
    password = json_data['password']
    print(json_data)
    print(username)
    print(password)
    user = authenticate(username=username, password=password)
    if user is not None:
        print('success log in')
        return HttpResponse(user.username, status=200)
    print('error log in')
    return HttpResponse(status=401)

@csrf_exempt
def authenticationCheck(request):
    print(request.user)
    if request.user.is_authenticated:
        print("is auth")
        return HttpResponse("is authenticated")
    else:
        print("is not auth")
        return HttpResponse("is not authenticated")
