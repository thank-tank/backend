from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse, JsonResponse
import json
from iotClient.models import Sensor

def index(request):
    print("Client Index")
    return HttpResponse("Client Index")

@csrf_exempt
def submitData(request):
    if request.method == "GET":
        sensor_data = Sensor.objects.all()
        label = sensor_data[0].sensor
        payload = [el.data for el in sensor_data]
        return JsonResponse({'label': label, 'data': payload })
    elif request.method == "POST":
        print("successful post method")
        print(request.body)
        json_data = json.loads(request.body)
        print(json_data)
        print(json_data['sensor'])
        print(json_data['data'])
        s = Sensor(sensor=json_data['sensor'], data=json_data['data'])
        s.save()
        return HttpResponse("success")
