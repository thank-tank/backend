from django.db import models
from user.models import User

class Drop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    pub_data = models.DateTimeField(auto_now_add=True)

class Drip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    pub_data = models.DateTimeField(auto_now_add=True)

