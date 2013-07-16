from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Player(models.Model):
    accepted = models.BooleanField()
    rejected = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    
    
class Move(models.Model):
    player = models.ForeignKey(Player)
    move = models.CharField(max_length=255)
    selectXY = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.move
