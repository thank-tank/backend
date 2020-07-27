from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse, JsonResponse
import json

def index(request):
    print("Client Index")
    return HttpResponse("Client Index")

@csrf_exempt
def submitData(request):
    if request.method == "GET":
        return JsonResponse({'data': [1, 2, 3]})
    elif request.method == "POST":
        print("successful post method")
        print(request.body)
        json_data = json.loads(request.body)
        print(json_data)
        print(json_data['sensor'])
        print(json_data['data'])
        return HttpResponse("success")
