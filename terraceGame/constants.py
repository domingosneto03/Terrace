import pygame

ROWS, COLS = 8, 8 # rows and columns
SQUARE_SIZE = 90 # square size -> to change window size: change square size

# board size according to the squares
WIDTH = SQUARE_SIZE * COLS
HEIGHT = SQUARE_SIZE * ROWS

# piece sizes
SIZE_BIG = 0.9
SIZE_MEDIUM = 0.8
SIZE_SMALL = 0.6
SIZE_SMALLER = 0.4

# colors in rgb
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 105, 180)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# grey for the board

GREY1 = (120, 120, 120) 
GREY2 = (121, 121, 121) 
GREY3 = (122, 123, 123) 
GREY4 = (124, 124, 124) 
GREY5 = (125, 125, 125) 
GREY6 = (126, 126, 126) 
GREY7 = (127, 127, 127) 
GREY8 = (128, 128, 128)

LIGHT_GREY1 = (203, 203, 203)
LIGHT_GREY2 = (204, 204, 204)
LIGHT_GREY3 = (205, 205, 205)  
LIGHT_GREY4 = (206, 206, 206)
LIGHT_GREY5 = (207, 207, 207)
LIGHT_GREY6 = (208, 208, 208)
LIGHT_GREY7 = (209, 209, 209)
LIGHT_GREY8 = (210, 210, 210)

# Color pattern of the board
COLOR_PATTERN = [
    [GREY1, LIGHT_GREY1, GREY2, LIGHT_GREY2, GREY3, LIGHT_GREY3, GREY4, LIGHT_GREY4],
    [LIGHT_GREY1, LIGHT_GREY1, GREY2, LIGHT_GREY2, GREY3, LIGHT_GREY3, GREY4, GREY4],
    [GREY2, GREY2, GREY2, LIGHT_GREY2, GREY3, LIGHT_GREY3, LIGHT_GREY3, LIGHT_GREY3],
    [LIGHT_GREY2, LIGHT_GREY2, LIGHT_GREY2, LIGHT_GREY2, GREY3, GREY3, GREY3, GREY3],
    [GREY5, GREY5, GREY5, GREY5, LIGHT_GREY7, LIGHT_GREY7, LIGHT_GREY7, LIGHT_GREY7],
    [LIGHT_GREY5, LIGHT_GREY5, LIGHT_GREY5, GREY5, LIGHT_GREY7, GREY7, GREY7, GREY7],
    [GREY6, GREY6, LIGHT_GREY5, GREY5, LIGHT_GREY7, GREY7, LIGHT_GREY8, LIGHT_GREY8],
    [LIGHT_GREY6, GREY6, LIGHT_GREY5, GREY5, LIGHT_GREY7, GREY7, LIGHT_GREY8, GREY8]
]