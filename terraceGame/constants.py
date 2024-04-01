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

# Level pattern of the board
BOARD_LEVEL_PATTERN = [
    [8, 7, 6, 5, 4, 3, 2, 1],
    [7, 7, 6, 5, 4, 3, 2, 2],
    [6, 6, 6, 5, 4, 3, 3, 3],
    [5, 5, 5, 5, 4, 4, 4, 4],
    [4, 4, 4, 4, 5, 5, 5, 5],
    [3, 3, 3, 4, 5, 6, 6, 6],
    [2, 2, 3, 4, 5, 6, 7, 7],
    [1, 2, 3, 4, 5, 6, 7, 8]
]

def LEVELS(color):
    if color == GREY1:
        return [(0,0)]
    elif color == LIGHT_GREY1:
        return [(1,0), (1,1), (0,1)]
    elif color == GREY2:
        return [(2,0), (2,1), (2,2), (1,2), (0,2)]
    elif color == LIGHT_GREY2:
        return [(3,0), (3,1), (3,2), (3,3), (2,3), (1,3), (0,3)]
    
    elif color == GREY3:
        return [(0,4), (1,4), (2,4), (3,4), (3,5), (3,6), (3,7)]
    elif color == LIGHT_GREY3:
        return [(0,5), (1,5), (2,5), (2,6), (2,7)]
    elif color == GREY4:
        return [(0,6), (1,6), (1,7)]
    elif color == LIGHT_GREY4:
        return [(0,7)]
    
    elif color == GREY5:
        return [(4,0), (4,1), (4,2), (4,3), (5,3), (6,3), (7,3)]
    elif color == LIGHT_GREY5:
        return [(5,0), (5,1), (5,2), (6,2), (7,2)]
    elif color == GREY6:
        return [(6,0), (6,1), (7,1)]
    elif color == LIGHT_GREY6:
        return [(7, 0)]
    
    elif color == LIGHT_GREY7:
        return [(7,4), (6,4), (5,4), (4,4), (4,5), (4,6), (4,7)]
    elif color == GREY7:
        return [(7,5), (6,5), (5,5), (5,6), (5,7)]
    elif color == LIGHT_GREY8:
        return [(7,6), (6,6), (6,7)]
    elif color == GREY8:
        return [(7,7)]
    else:
        return 0