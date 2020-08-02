import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from drop.models import Drip, Drop
from user.models import User

@csrf_exempt
def post_drop(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        user = User.objects.get(username=json_data['username'])
        if user is not None:
            author = User.objects.get(username=json_data['username'])
            drop = Drop(user=author, content=json_data['content'])
            drop.save()
            return HttpResponse(status=201)
        return HttpResponse(status=401)

@csrf_exempt
def post_drip(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        user = User.objects.get(username=json_data['username'])
        if user is not None:
            author = User.objects.get(username=json_data['username'])
            drop = Drop.objects.get(id=json_data['drop_id'])
            response = Drip(user=author, drop=drop, content=json_data['content'])
            response.save()
            return HttpResponse(status=201)
        return HttpResponse(status=401)

@csrf_exempt
def get_ocean(request):
    if request.method == "GET":
        ocean = Drop.objects.all().order_by('-pub_data').values()
        for drop in ocean:
            drip = Drip.objects.filter(drop_id=drop['id']).values()
            drop['username'] = User.objects.get(id=drop['user_id']).username
            drop['drip_stream'] = list(drip)
        return JsonResponse({"ocean": list(ocean)})

@csrf_exempt
def get_user_stream(request, username):
    if request.method == "GET":
        user = User.objects.get(username=username)
        ocean = Drop.objects.all().filter(user_id=user.id).order_by('-pub_data').values()
        for drop in ocean:
            drip = Drip.objects.filter(drop_id=drop['id']).values()
            drop['username'] = User.objects.get(id=drop['user_id']).username
            drop['drip_stream'] = list(drip)
        return JsonResponse({"ocean": list(ocean)})

@csrf_exempt
def get_drop(request, drop_id):
    print("GET DROP")
    if request.method == "GET":
        drop = Drop.objects.get(id=drop_id)
        print(drop)
        ret = {
            "username": drop.user.username,
            "pub_data": drop.pub_data,
            "content": drop.content,
            "drip_stream": []
        }
        drip_stream = Drip.objects.filter(drop_id=drop_id).values()
        for drip in drip_stream:
            drip['username'] = User.objects.get(id=drip['user_id']).username
            ret['drip_stream'].append(drip)
        print(ret)
        return JsonResponse(ret)

@csrf_exempt
def get_total_drops(request):
    if request.method == "GET":
        return JsonResponse({"total": len(Drop.objects.all())})
