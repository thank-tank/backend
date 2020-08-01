from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
import json
from post.models import Post, Response
from user.models import User

@csrf_exempt
def makePost(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        user = authenticate(username=json_data['username'], password=json_data['password'])
        if user is not None:
            author = User.objects.get(username=json_data['username'])
            post = Post(user=author, content=json_data['content'])
            post.save()
            return HttpResponse(status=201)
        return HttpResponse(status=401)

@csrf_exempt
def makeResponse(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        user = authenticate(username=json_data['username'], password=json_data['password'])
        if user is not None:
            author = User.objects.get(username=json_data['username'])
            post = Post.objects.get(id=json_data['post_id'])
            response = Response(user=author, post=post, content=json_data['content'])
            response.save()
            return HttpResponse(status=201)
        return HttpResponse(status=401)

@csrf_exempt
def getFeed(request):
    if request.method == "GET":
        feed = Post.objects.all().values()
        for post in feed:
            responses = Response.objects.filter(post_id=post['id']).values()
            post['post_feed'] = list(responses)
        return JsonResponse({"feed": list(feed)})
