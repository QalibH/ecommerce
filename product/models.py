from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)

def __str__(self):
    return self.name

class Blog(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/')
