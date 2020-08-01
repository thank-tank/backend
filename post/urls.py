from django.urls import path

from . import views

urlpatterns = [
    path('', views.makePost, name='create_post'),
    path('response', views.makeResponse, name='create_response'),
    path('feed', views.getFeed, name='get_feed')
]
