import pygame
from terraceGame.constants import *
from terraceGame.board import Board

FPS = 60 # frames per second

pygame.font.init() # just to be able to write in the pieces

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Terrace')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            # turn off
            if event.type == pygame.QUIT:
                run = False

            # select with mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 3, 3) 

        board.draw_board(WIN)
        pygame.display.update()
    
    pygame.quit()

main()