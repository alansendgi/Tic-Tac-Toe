from django.db import models
import datetime
from django.utils import timezone
"""
Still contains left-overs from the 'Polls' tutorial, 
but I adapted them to make this app work.

see https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style
for some ideas
"""


class Game(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.question


class Board(models.Model):
    """
    Initialize all game pieces, both players, etc. We're not using zero (0) here 
    to avoid confusion with the letter 'O'.
    I've assigned player_O to be the computer to avoid creating user accounts, etc.
    """
    def __init__(self):
        self.move_names = '123456789'
        self.free_move = ' '
        self.player_X = 'x'
        self.player_O = 'o'
        self.moves = [self.free_move]*9
    
    _winning_rows = [[1,2,3],[4,5,6],[7,8,9], # horizontal
                    [1,4,7],[2,5,8],[3,6,9],  # vertical
                    [1,5,9],[3,5,7]]          # diagonals
    
    def winner(self):
        """
        Needs work
        """
        
        
class Choice(models.Model):
    """
    Needs work
    """
    game = models.ForeignKey(Game)
    choice_text = models.CharField(max_length=200)
    totals = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice_text
    
    
class Player(object):
    """
    Needs work
    """
    
    
