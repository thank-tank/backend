from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_drop, name='create_drop'),
    path('drip', views.post_drip, name='create_drip'),
    path('ocean', views.get_ocean, name='get_ocean'),
    path('ocean/<str:username>/', views.get_user_stream, name='get_user_stream'),
    path('<int:drop_id>/', views.get_drop, name='get_drop'),
    path('ocean/total', views.get_total_drops, name='get_total_drops'),
]
