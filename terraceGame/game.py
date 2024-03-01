import pygame
from terraceGame.constants import *
from terraceGame.board import Board

class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.valid_moves = {}
        self.win = win

    def update(self):
        self.board.draw_board(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece !=0 and piece.get_color() == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False
    
    def _move(self, new_row, new_col):
        piece = self.board.get_piece(new_row, new_col)
        if self.selected and piece == 0 and (new_row, new_col) in self.valid_moves:
            self.board.move(self.selected, new_row, new_col)
            self.change_turn()

        elif self.selected and piece != 0 and (new_row, new_col) in self.valid_moves:
            target = self.valid_moves[(new_row, new_col)]
            if target:
                self.board.remove(target)
                self.board.move(self.selected, new_row, new_col)
            self.change_turn()

        else:
            return False
        
        return True
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLUE:
            self.turn = RED
        else:
            self.turn = BLUE
        return self.turn

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN,  (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 10)