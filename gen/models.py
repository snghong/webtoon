from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

    

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    details = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.name
    
class Context(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=20)
    details = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.location

class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length = 800)
    num_panels = models.IntegerField()

    def __str__(self):
        return self.title
    
class Segment(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return "segment"
    