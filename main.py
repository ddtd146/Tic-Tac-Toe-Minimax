import pygame as p
import sys
from constants import *
from game import *
import os

# p setup

#main 
def main():
  
  player1 = Player("Dung", CROSS)
  player2 = Player("Thang", CIRCLE)
  game = Game(player1, player2)
  os.environ['SDL_VIDEO_CENTERED'] = '1'
  p.init()
  game.run()

main()
