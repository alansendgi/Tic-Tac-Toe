from django.db import models
import datetime
from django.utils import timezone


class Board(models.Model):
    """Represents tic tac toe board. We're not using zero (0) here 
    to avoid confusion with the letter 'O'"""
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
        """Winning combinations. Returns Player or None"""
        for row in Board._winning_rows:
            if self.moves[row[0]] != self.free_move and self.allEqual([self.moves[i] for i in row]):
                return self.moves[row[0]]

    def allEqual(self, list):
        """returns True if all the elements in a list are equal, or if the list is empty."""
        return not list or list == [list[0]] * len(list)

    def getValidMoves(self):
        """Returns list of valid moves"""
        return [pos for pos in range(9) if self.moves[pos] == self.free_move]

    def gameOver(self):
        return bool(self.winner()) or not self.getvalidvoves()
        
    def startover(self):
        """Clears board"""
        self.moves = [self.free_move]*9


class Choice(models.Model):
    game = models.ForeignKey(Game)
    choice_text = models.CharField(max_length=200)
    totals = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice_text
    
    
class Player(object):
    """ Represents player and his/her moves"""
    '''may want to put this under Choice, or vice versa'''
    def __init__(self, piece, moves):
        self.moves = moves
        self.piece = piece

    def get_move(self):
        print("Move Player %s" % self.piece) #this print statement goes in views.py
        
    def make_move(self, move):
        """Plays a move. Note: this doesn't check if the move is legal!"""
        self.moves[move] = player
    
    def __str__(self):
        return "Player " + self.piece


class Game(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.question



