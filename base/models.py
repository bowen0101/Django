from turtle import onclick, update
from django.db import models
from django.contrib.auth.models import User



class Topic(models.Model):
    name = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name

# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # null is manily for database, it could be a instance 
    description = models.TextField(null=True, blank=True)
    # participants = 
    update = models.DateField(auto_now = True)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', '-create']


    def __str__(self):
        return self.name 


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateField(auto_now = True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    

