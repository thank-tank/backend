from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    print("Client Index")
    return HttpResponse("Client Index")
