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
GREY = (128, 128, 128)
LIGHT_GREY = (211, 211, 211)
PINK = (255, 105, 180)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# gradient of grey for the board: darker to lighter

GREY1 = (25, 25, 25) 
GREY2 = (50, 50, 50) 
GREY3 = (90, 90, 90) 
GREY4 = (130, 130, 130) 
GREY5 = (170, 170, 170) 
GREY6 = (200, 200, 200) 
GREY7 = (235, 235, 235) 
GREY8 = (250, 250, 250)  

# Color pattern of the board
COLOR_PATTERN = [
    [GREY, LIGHT_GREY, GREY, LIGHT_GREY, GREY, LIGHT_GREY, GREY, LIGHT_GREY],
    [LIGHT_GREY, LIGHT_GREY, GREY, LIGHT_GREY, GREY, LIGHT_GREY, GREY, GREY],
    [GREY, GREY, GREY, LIGHT_GREY, GREY, LIGHT_GREY, LIGHT_GREY, LIGHT_GREY],
    [LIGHT_GREY, LIGHT_GREY, LIGHT_GREY, LIGHT_GREY, GREY, GREY, GREY, GREY],
    [GREY, GREY, GREY, GREY, LIGHT_GREY, LIGHT_GREY, LIGHT_GREY, LIGHT_GREY],
    [LIGHT_GREY, LIGHT_GREY, LIGHT_GREY, GREY, LIGHT_GREY, GREY, GREY, GREY],
    [GREY, GREY, LIGHT_GREY, GREY, LIGHT_GREY, GREY, LIGHT_GREY, LIGHT_GREY],
    [LIGHT_GREY, GREY, LIGHT_GREY, GREY, LIGHT_GREY, GREY, LIGHT_GREY, GREY]
]

COLOR_PATTERN2 = [
    [GREY1, GREY2, GREY3, GREY4, GREY5, GREY6, GREY7, GREY8],
    [GREY2, GREY2, GREY3, GREY4, GREY5, GREY6, GREY7, GREY7],
    [GREY3, GREY3, GREY3, GREY4, GREY5, GREY6, GREY6, GREY6],
    [GREY4, GREY4, GREY4, GREY4, GREY5, GREY5, GREY5, GREY5],
    [GREY5, GREY5, GREY5, GREY5, GREY4, GREY4, GREY4, GREY4],
    [GREY6, GREY6, GREY6, GREY5, GREY4, GREY3, GREY3, GREY3],
    [GREY7, GREY7, GREY6, GREY5, GREY4, GREY3, GREY2, GREY2],
    [GREY8, GREY7, GREY6, GREY5, GREY4, GREY3, GREY2, GREY1]
]
