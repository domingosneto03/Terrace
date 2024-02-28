import pygame
from terraceGame.constants import *
from terraceGame.board import Board

FPS = 60 # frames per second

pygame.font.init() # just to be able to write in the pieces

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Terrace')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    #testing
    piece = board.get_piece(1,3)
    board.move(piece, 2, 3)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            # turn off
            if event.type == pygame.QUIT:
                run = False

            # for later
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_board(WIN)
        pygame.display.update()
    
    pygame.quit()

main()