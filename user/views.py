from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import json

@csrf_exempt
def register(request):
    if request.method == "POST":
        print(request.body)
        json_data = json.loads(request.body)
        email = json_data['email']
        password = json_data['password']
        print(json_data)
        print(email)
        print(password)
        #user = User(email=email, password=password, jwt="fake_jwt" + email)
        user = User.objects.create_user(email=email, username=email, password=password)
        user.save()
        return HttpResponse(status=201)

@csrf_exempt
def loginAttempt(request):
    print(request.body)
    json_data = json.loads(request.body)
    email = json_data['email']
    password = json_data['password']
    print(json_data)
    print(email)
    print(password)
    user = authenticate(username=email, password=password)
    if user is not None:
        print('success log in')
        login(request, user)
        return HttpResponse(user.email, status=200)
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
