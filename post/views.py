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
        user = User.objects.get(username=json_data['username'])
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
        user = User.objects.get(username=json_data['username'])
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
        feed = Post.objects.all().order_by('-pub_data').values()
        for post in feed:
            responses = Response.objects.filter(post_id=post['id']).values()
            post['username'] = User.objects.get(id=post['user_id']).username
            post['post_feed'] = list(responses)
        return JsonResponse({"feed": list(feed)})

@csrf_exempt
def getDrop(request, post_id):
    print("GET DROP")
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        print(post)
        ret = {
            "username": post.user.username,
            "pub_data": post.pub_data,
            "content": post.content,
            "post_feed": []
        }
        responses = Response.objects.filter(post_id=post_id).values()
        for response in responses:
            response['username'] = User.objects.get(id=response['user_id']).username
            ret['post_feed'].append(response)
        print(responses)
        return JsonResponse(ret)

@csrf_exempt
def getTotalDrops(request):
    if request.method == "GET":
        print(len(Post.objects.all()))
        return JsonResponse({"total": len(Post.objects.all())})
