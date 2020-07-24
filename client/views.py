from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def index(request):
    print("Client Index")
    return HttpResponse("Client Index")

def getData(request, device_id):
    if request.method == "GET":
        return JsonResponse({'data': [1, 2, 3]})
    elif request.method == "POST":
        return HttpResponse(str(device_id))
