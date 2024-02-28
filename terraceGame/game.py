import pygame
from terraceGame.constants import *
from terraceGame.board import Board

class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.win = win

    def update(self):
        self.board.draw_board(self.win)
        pygame.display.update()