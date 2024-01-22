class Player:
  def __init__(self, name, xo, score=0):
    self.name = name
    self.xo = xo
    self.score = score
  def copy(self):
    return Player(self.name, self.xo, self.score)