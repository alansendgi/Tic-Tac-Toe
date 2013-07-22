from django.db import models


class Board(models.Model):
    ''' 
    '''
    """Represents tic tac toe board"""
    def __init__(self):
        self.move_names = '012345678'
        self.free_move = ' '
        self.player_X = 'x'
        self.player_O = 'o'
        self.moves = [self.free_move]*9
    
    _winning_rows = [[0,1,2],[3,4,5],[6,7,8], # up and down
                    [0,3,6],[1,4,7],[2,5,8],  # across
                    [0,4,8],[2,4,6]]          # diagonal
    
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
    
    
class Player(models.Model):
    ''' 
    '''
    """ Represents player and his/her moves"""
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
    ''' move all messages to views.py
    '''
    _welcome_mes = """Welcome to Tic Tac Toe!

    The Game board is as follows:

    _0_|_1_|_2_
    _3_|_4_|_5_
     6 | 7 | 8   """

    def __init__(self):
        self.board = Board()
        self.playerX = Player('x', self.board.moves)
        self.playerO = Player('o', self.board.moves)
        self._currentTurn = self.playerX

    def _swapCurrentTurn(self):
        if self._currentTurn == self.playerX:
            self._currentTurn = self.playerO
        else: self._currentTurn = self.playerX

    def start(self):
        print(Game._welcome_mes)
        while not self.isGameOver():
            print("Turn: " + str(self._currentTurn))
            if self._currentTurn.move():
                self._swapCurrentTurn()
        self._atGameEnd()

    def _atGameEnd(self):
        print(self.board.winner() + " has won the game")
        print("Would you like to play again?")
        answer = input()
        if str(answer).lower() in ["yes", "y", "yeah"]:
            self._restart()

    def _restart(self):
        self.board.clear()
        self.playerX = Player('x', self.board.moves)
        self.playerO = Player('o', self.board.moves)
        self._currentTurn = self.playerX        

    def isGameOver(self):
        return self.board.gameOver()
