from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.loginAttempt, name='login'),
    path('all', views.get_users, name='all'),
]
