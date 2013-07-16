from django.db import models
import random

class Game(models.Model):
    # Define Game class
    pass

    # I think these go to views.py
    # sets up game board, and assigns game piece.
    def drawBoard(board):
        pass
    
    def getPlayerLetter():
        # Let the human choose which letter they want to be.
        # Returns a list with the player's letter as the first item, 
        # and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()
        
    
class Move(models.Model):
    # define the Move class to track game playing
    move = models.CharField(max_length=255)
    select_square = models.PositiveSmallIntegerField()
    
    def __unicode__(self):
        return self.move, self.select_square
