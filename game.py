from constants import *
import numpy as np
from ai import *
from board import *
from player import *


class Game: 
  def __init__(self, player1, player2):
    self.board = Board()
    self.ai = AI("AI")
    player0 = Player("No one", 0)
    self.player1 = player1
    self.player2 = player2
    self.players = [player0, player1, player2]
    self.players[1].score = 0
    self.players[2].score = 0
    self.playing = CROSS
    self.over = None
    self.winner = None
    self.gamemode = 'pvp'
    
  def next_turn(self):
    self.playing =  CROSS + CIRCLE - self.playing
    
  def make_move(self, pos, to_play):
    self.board.mark_sqr(pos, to_play)
  
  def update_state(self, pos):
    if pos == None: 
      return
    self.make_move(pos, self.playing)
    
    result = int(self.board.check_state())
    if self.board.isFull() or result != 0:
      self.winner = self.end_game(result).copy()
    self.next_turn()
  
  def end_game(self, result):
    self.over = True
    for i in range(3): 
      if (self.players[i].xo == result): 
        self.players[i].score += 1
        return self.players[i]
    return None

  def switch_first_to_play(self):
    self.players[1].xo = (CROSS + CIRCLE - self.players[1].xo)
    self.players[2].xo = (CROSS + CIRCLE - self.players[2].xo)
  
  def change_mode(self, mode):
    self.gamemode = mode
    if mode == 'ai':
      self.players[2] = self.ai
    if mode == 'pvp':
      self.players[1] = self.player1
      self.players[2] = self.player2
    self.players[1].score = 0
    self.players[2].score = 0
  
  def new_game(self):
    self.__init__(self.players[1], self.players[2])
    
  def restart(self):
    self.board = Board()  
    self.playing = CROSS
    self.over = None
  
  def start_game(self):
    self.over = False
  
  def process_input(self):
    for event in p.event.get():
      # quit event
      if event.type == p.QUIT:
          p.quit()
          sys.exit()
      
      # keydown event to handle all game functions: restart, newgame, changemode,...
      if event.type == p.KEYDOWN and self.over != False:
        if event.key == p.K_r:
          self.restart()
        if event.key == p.K_s:
          self.switch_first_to_play()
        if event.key == p.K_p:
          self.change_mode('pvp')
        if event.key == p.K_b:
          self.change_mode('ai')  
        if event.key == p.K_RETURN:
          self.start_game()
        if event.key == p.K_n:
          self.new_game()
        if self.gamemode == 'ai': 
          if event.key == p.K_0:
            self.ai.change_level(0)
          if event.key == p.K_1:
            self.ai.change_level(1)
          if event.key == p.K_2:
            self.ai.change_level(2)
          if event.key == p.K_3:
            self.ai.change_level(3)
                  
      # click event
      if event.type == p.MOUSEBUTTONDOWN and self.over == False and (self.playing != self.ai.xo or self.gamemode == 'pvp'):
        pos = event.pos
        if pos[1] <= BOARD_HEIGHT and pos[0] <= BOARD_WIDTH:
          row = pos[1] // (SQSIZE + LINE_WIDTH)
          col = pos[0] // (SQSIZE + LINE_WIDTH)
          return (row, col)
    return None
  
  def run(self):
    self.render_window()
    while(True):
      pos = self.process_input()
      if self.gamemode == 'ai' and self.playing == self.ai.xo and self.over == False:
        pos = self.ai.decide(self.board)
      self.update_state(pos)
      self.render_board()
      self.render_score()
      if self.over == True:
        self.render_winner()
      p.display.update()
      p.time.delay(60)
  
  def render_window(self): 
    self.window = p.display.set_mode((WIDTH, HEIGHT))
    self.game_board = self.window.subsurface((0, 0, BOARD_WIDTH, BOARD_HEIGHT))
    self.score_board = self.window.subsurface((BOARD_WIDTH, 0, 200, BOARD_HEIGHT))
    p.display.set_caption('TIC TAC TOE AI')
    self.window.fill(BG_COLOR)
  
  def render_board(self):
    self.window.fill(BG_COLOR)
    # render board view
    for i in range(ROWS):
      for j in range(COLS): 
        # render top-left corner of each square
        square_x = j * (SQSIZE + LINE_WIDTH)
        square_y = i * (SQSIZE + LINE_WIDTH)
        # draw
        if self.board.sqrs[i][j] == CIRCLE:
          p.draw.circle(self.game_board, O_COLOR, (SQSIZE//2 + square_x, SQSIZE//2 + square_y), RADIUS, LINE_WIDTH)
        if self.board.sqrs[i][j] == CROSS:
          p.draw.line(self.game_board, X_COLOR, (square_x + PADDING_X_O, square_y + PADDING_X_O), (square_x + SQSIZE - PADDING_X_O, square_y + SQSIZE - PADDING_X_O), LINE_WIDTH)
          p.draw.line(self.game_board, X_COLOR, (square_x + PADDING_X_O, square_y + SQSIZE - PADDING_X_O), (square_x + SQSIZE - PADDING_X_O, square_y + PADDING_X_O), LINE_WIDTH)
    # show lines
    # vertical
    for i in range(COLS):
      p.draw.line(self.game_board, LINE_COLOR, ((i+1) * SQSIZE + (i*2+1) * LINE_WIDTH/2, 0), ((i+1) * SQSIZE + (i*2 + 1) * LINE_WIDTH/2, HEIGHT), width=LINE_WIDTH)
    # horizontal
    for i in range(ROWS):
      p.draw.line(self.game_board, LINE_COLOR, (0, (i+1) * SQSIZE + (2*i+1) * LINE_WIDTH/2), (HEIGHT, (i+1) * SQSIZE + (2*i+1) * LINE_WIDTH/2), width=LINE_WIDTH)
  
  def render_score(self):
    font = p.font.SysFont('comicsans', 20, True)
    text_name1 = font.render(self.players[1].name + " " + str(self.players[1].score), True, TEXT_COLOR)
    text_name2 = font.render(self.players[2].name + " " + str(self.players[2].score), True, TEXT_COLOR)
    self.score_board.blit(text_name1, (0, 0))
    self.score_board.blit(text_name2, (0, 50))
  
  def render_winner(self):
    font = p.font.SysFont('comicsans', 20, True)
    text = font.render(self.winner.name + " wins", True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    self.window.blit(text, text_rect)
  
  