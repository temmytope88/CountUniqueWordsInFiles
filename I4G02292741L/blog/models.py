from time import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    Text = models.TextField()
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(default=timezone.now)
    
