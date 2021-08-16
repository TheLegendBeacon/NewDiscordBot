import random

class grid:
  def __init__(self, player1, player2):
    self.grid = {self.a: [None, None, None], 
    self.b: [None, None, None], 
    self.c: [None, None,None]
    }
    self.totalList = self.a + self.b + self.c

    self.players = [player1, player2]

class User():
    def __init__(self, player):
        self.id = player.id
        self.name = player.name
        self.score = 0
        self.side = ChooseSide()
        if self.side == 0:
            self.letter = 'O'
        else:
            self.letter = 'X'

def ChooseSide(chosen=False, prevside=None):
    if chosen == False:
        x = random.randrange(0, 2)
        return x
    else:
        if prevside == 1:
            return 0
        if prevside == 0:
            return 1

def collections(self: grid):
  collectionslist = [
  [self.a[0], self.a[1], self.a[2]], [self.b[0], self.b[1], self.b[2]], [self.c[0], self.c[1], self.b[2]], [self.a[0], self.b[1], self.c[2]], [self.c[0], self.b[1], self.a[2]], [self.a[0], self.b[0], self.c[0]], [self.a[1], self.b[1], self.c[1]], [self.a[2], self.b[2], self.c[2]]]
  return collectionslist

def winCheck(self: grid):
  collectionList = collections(self)
  for record in collectionList:
    for item in record:
      if item == "x":
        collectionList[collectionList.index(record)][record.index(item)] = 2
      elif item == "o":
        collectionList[collectionList.index(record)][record.index(item)] = 1
    if None not in collectionList:
      if sum(collectionList) == 3:
        return (True, "o")
      elif sum(collectionList) == 6:
        return (True, "x")
      else:
        return False
    else:
      pass
  return False


def tieCheck(self: grid):
  if '-' in self.totalList():
    return False
  else:
    return True