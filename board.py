import pygame as p
from constants import *
import numpy as np

class Board: 
  ## player 1 -> X
  ## player 2 -> O
  def __init__(self):
    self.sqrs = np.zeros((ROWS, COLS), dtype=int)
    self.marked_nsqrs = 0
    self.last_move = None
  
  #check whether state is win or not
  def check_state(self) -> int:
    '''
      @return 0 if there is no win 
      @return 1 if player X win 
      @return 2 if player O win 
    '''
    #vertical check
    for col in range(COLS):
      for row in range(ROWS):
        r = 0
        for i in range(WIN_COND):
          if row + i < ROWS and self.sqrs[row][col] == self.sqrs[row+i][col] != 0:
            r = r + 1;
        if r == WIN_COND:
          return self.sqrs[row][col]
    #horizontal check
    for row in range(ROWS):
      for col in range(COLS):
        r = 0
        for i in range(WIN_COND):
          if col + i < COLS and self.sqrs[row][col] == self.sqrs[row][col+i] != 0:
            r = r + 1
        if r == WIN_COND:
          return self.sqrs[row][col]
    #diagonal check
    for row in range(ROWS):
      for col in range(COLS):
        r = 0
        tnc = 0
        for i in range(WIN_COND):
          if col + i < COLS and row + i < ROWS and self.sqrs[row][col] == self.sqrs[row+i][col+i] != 0:
            r = r + 1
          if col - i >= 0 and row + i < ROWS and self.sqrs[row][col] == self.sqrs[row+i][col-i] != 0:
            tnc = tnc + 1
        if r == WIN_COND or tnc == WIN_COND:
          return self.sqrs[row][col]
    return 0
  
  def mark_sqr(self, pos, to_play):
    row = pos[0]
    col = pos[1]
    if self.sqrs[row][col] == 0:
      self.sqrs[row][col] = to_play
      
      self.marked_nsqrs += 1
  
  def isEmptyGrid(self, row, col): 
    return self.sqrs[row][col] == 0
  
  def get_empty_sqrs(self):
    empty_sqrs = []
    for row in range(ROWS):
      for col in range(COLS):
        if self.isEmptyGrid(row, col):
          empty_sqrs.append((row, col))
    return empty_sqrs
  
  def isFull(self):
    return self.marked_nsqrs == ROWS * COLS
  
  def isEmpty(self):
    return self.marked_sqrs == 0
  

  
  
    