from django.urls import path

from . import views

urlpatterns = [
    path('', views.makePost, name='create_post'),
    path('response', views.makeResponse, name='create_response'),
    path('feed', views.getFeed, name='get_feed'),
    path('drop/<int:post_id>/', views.getDrop, name='get_drop'),
    path('total', views.getTotalDrops, name='get_total_drops'),
]
