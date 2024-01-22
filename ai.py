import pygame as p
import sys
from constants import *
import numpy as np
import random
import copy
from player import *
from heuristic import *

class AI(Player):

  def __init__(self, name, score=0, xo=CIRCLE):
    super().__init__(name, xo, score)
    self.level = 0
  
  def change_level(self, level):
    self.level = level
  
  def get_options(self, board):
    empty_sqrs = board.get_empty_sqrs()
    return empty_sqrs
  
  def rnd(self, board):
    empty_sqrs = board.get_empty_sqrs()
    i = random.randrange(0, len(empty_sqrs))
    return empty_sqrs[i]
  
  def minimax(self, depth, board, alpha, beta, maxplayer=True):
    game_state = board.check_state();
    if depth == 0 or game_state != 0 or board.isFull():
      return basic_eval(board), None
    
    options = self.get_options(board)
    if maxplayer:
      maxEval = -1000
      best_move = None
      for option in options:
        temp_board = copy.deepcopy(board)
        temp_board.mark_sqr(option, CROSS)
        val = self.minimax(depth-1, temp_board, alpha, beta, False)[0]
        if maxEval < val: 
          maxEval = val
          best_move = option
        alpha = max(alpha, val)
        if beta <= alpha:
          break
      return (maxEval, best_move)
    
    minEval = 1000
    best_move = None
    for option in self.get_options(board):
      temp_board = copy.deepcopy(board)
      temp_board.mark_sqr(option, CIRCLE)
      val = self.minimax(depth-1, temp_board, alpha, beta, True)[0]
      if minEval > val: 
          minEval = val
          best_move = option
      beta = min(beta, val)
      if beta <= alpha:
        break
    return (minEval, best_move)
  
  def decide(self, board): 
    if self.level == 0:
      self.move = self.rnd(board)
    else:
      # force move
      self.move = self.minimax(self.level, board, -1000, 1000, (self.xo == CROSS))[1]
    return self.move