
BOARD_WIDTH = 600
BOARD_HEIGHT =  600


SCORE_WIDTH = 200
SCORE_HEIGHT = 600

WIDTH = BOARD_WIDTH + SCORE_WIDTH
HEIGHT = BOARD_HEIGHT


ROWS = 3
COLS = 3

LINE_WIDTH = 1
SQSIZE = (BOARD_WIDTH - (ROWS - 1)*LINE_WIDTH) // COLS

# COLORS
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
O_COLOR = (255, 0, 0)
X_COLOR = (0, 0, 0)
TEXT_COLOR = (30, 30, 30)
# O 
PADDING_X_O = 2
RADIUS = SQSIZE // 2 - PADDING_X_O


#
CROSS = 1
CIRCLE = 2 

#

WIN_COND = 3


#
EVAL = [0, 1, 10, 100, 1000, 10000]

