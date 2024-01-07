from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default=user.name)
    text = models.CharField(max_length = 800)
    num_chapters = models.IntegerField(default=4)
    pub_date =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

class Character(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    details = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Context(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    location = models.CharField(max_length=20)
    details = models.CharField(max_length=200)
    pub_date =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.location


class Chapter(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    mood = models.CharField(max_length=200)
    chapter_name = models.CharField(max_length=200)
    chapter_num = models.IntegerField(default=1)
    pub_date =  models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Chapter {self.chapter_num}: {self.chapter_name}"
    

class Panel(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    mood = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    dialogue = models.CharField(max_length=200)
    sfx = models.CharField(max_length=200)
    def __str__(self):
        return "Panel"
    