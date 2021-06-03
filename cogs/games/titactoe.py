class grid:
  def __init__(self, player1, player2):
    self.grid = {self.a: [None, None, None], 
    self.b: [None, None, None], 
    self.c: [None, None,None]
    }

    self.players = [player1, player2]

class User:
  def __init__(self, user):
    self.id = user.id
    self.name = user.name

def winCheck(player: User, self: grid):
    conditions = [
        self.a[0] == player.letter and self.a[1] == player.letter and self.a[2] == player.letter, 
        self.b[0] == player.letter and self.b[1] == player.letter and self.b[2] == player.letter,
        self.c[0] == player.letter and self.c[1] == player.letter and self.c[2] == player.letter, 
        self.a[0] == player.letter and self.b[1] == player.letter and self.c[2] == player.letter,
        self.c[0] == player.letter and self.b[1] == player.letter and self.a[2] == player.letter, 
        self.a[0] == player.letter and self.b[0] == player.letter and self.c[0] == player.letter,
        self.a[1] == player.letter and self.b[1] == player.letter and self.c[1] == player.letter, 
        self.a[2] == player.letter and self.b[2] == player.letter and self.c[2] == player.letter
    ]
    for condition in conditions:
        if condition:
            return True
            break

def possibleWin(self: grid):
  conditions = [
        self.a[0] == player.letter and self.a[1] == player.letter and self.a[2] == player.letter, 
        self.b[0] == player.letter and self.b[1] == player.letter and self.b[2] == player.letter,
        self.c[0] == player.letter and self.c[1] == player.letter and self.c[2] == player.letter, 
        self.a[0] == player.letter and self.b[1] == player.letter and self.c[2] == player.letter,
        self.c[0] == player.letter and self.b[1] == player.letter and self.a[2] == player.letter, 
        self.a[0] == player.letter and self.b[0] == player.letter and self.c[0] == player.letter,
        self.a[1] == player.letter and self.b[1] == player.letter and self.c[1] == player.letter, 
        self.a[2] == player.letter and self.b[2] == player.letter and self.c[2] == player.letter
  ]