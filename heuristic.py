import pygame as p
from constants import *
import numpy as np
from board import *

def naive_eval(board):
  winner = board.check_state()
  # x wins
  if winner == 1:
    return 1

  # o wins
  if winner == 2:
    return -1

  # draw
  return 0

def basic_eval_by_line(arr):
  # 000
  if arr[0] == arr[1] == arr[2] == 0: 
    return 0 
  # 111 or 222
  if arr[0] == arr[1] == arr[2] != 0: 
    return 100 if arr[0] == CROSS else -100
  # 011 or 110 or 022 or 220
  if (arr[0] == arr[1] != 0 and arr[2] == 0) or (arr[0] == 0 and arr[1] == arr[2] != 0):
    return 10 if arr[1] == CROSS else -10
  # 100 or 010 or 001 or 200 or 020 or 002
  if arr[0] == arr[1] == 0 or arr[1] == arr[2] == 0 or arr[0] == arr[2]:
    return 1 if arr[1] == CROSS or arr[2] == CROSS else -1
  return 0

def basic_eval(board):
  val = 0
  # eval each row and col
  for i in range(3): val += basic_eval_by_line(board.sqrs[i][:]) + basic_eval_by_line(board.sqrs[:][i])
  # extract main diagonal and sub-diagonal
  main_dia = [board.sqrs[i][i] for i in range(3)]
  sub_dia = [board.sqrs[i][2 - i] for i in range(3)]
  val += basic_eval_by_line(main_dia) + basic_eval_by_line(sub_dia)
  return val
# not done yet
def advanced_eval(board):
  val = 0
  cnt = [0, 0, 0, 0, 0, 0]
  for row in range(ROWS):
    for col in range(COLS):
      for j in range(1, WIN_COND+1, 1):
        r = np.zeros(shape=(3, 4), dtype=int)
        for i in range(j):
          if row + i < ROWS and board.squares[row][col] == board.squares[row+i][col] != 0:
            r[board.squares[row][col]][0] += 1
          if col + i < COLS and board.squares[row][col] == board.squares[row][col+i] != 0:
            r[board.squares[row][col]][1] += 1
          if row + i < ROWS and col + i < COLS and board.squares[row][col] == board.squares[row+i][col+i] != 0:
            r[board.squares[row][col]][2] += 1
          if row + i < ROWS and col - i >= 0 and board.squares[row][col] == board.squares[row+i][col-i] != 0:
            r[board.squares[row][col]][3] += 1
        for i in range(4):
          if r[CROSS][i] == j: 
            cnt[j] += 1
          if r[CIRCLE][i] == j:
            cnt[j] -= 1


  cnt[4] -= 2 * cnt[5]
  cnt[3] -= 2 * cnt[4] + 3 * cnt[5]
  cnt[2] -= 2 * cnt[3] + 3 * cnt[4] + 4 * cnt[5]
  cnt[1] -= 2 * cnt[2] + 3 * cnt[3] + 4 * cnt[4] + 5 * cnt[5]
  cnt[1] = cnt[1] // 4;
  val = np.array([cnt[i] * EVAL[i] for i in range(len(cnt))]).sum()
  return val