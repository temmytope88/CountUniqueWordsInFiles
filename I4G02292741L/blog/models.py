from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    Created_date = models.DateTimeField('date created')
    Published_date = models.DateTimeField('date published')
    
