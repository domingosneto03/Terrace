import pygame
from terraceGame.constants import *
from terraceGame.board import Board

class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = BLUE
        self.valid_moves = {}
        self.win = win # window not winner/wins

    def update(self):
        self.board.draw_board(self.win)
        self.draw_valid_moves(self.valid_moves, self.turn)
        pygame.display.update()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        piece = self.board.get_piece(row, col)
        if piece != None and piece.get_color() == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False
    
    def _move(self, new_row, new_col):
        piece = self.board.get_piece(new_row, new_col)

        # moving to a empty space
        if self.selected and piece == None and (new_row, new_col) in self.valid_moves:
            self.board.move(self.selected, new_row, new_col)  
            
            self.change_turn()

        # moving to a space with a piece
        elif self.selected and piece != None and (new_row, new_col) in self.valid_moves:
            target = self.valid_moves[(new_row, new_col)]
            if target:
                self.board.remove(target)
                if target.get_color() != self.selected.get_color():
                    self.board.calculate_pieces_captured(self.selected.get_color()) # calculate pieces captured by the player
                self.board.move(self.selected, new_row, new_col)
                
                
            self.change_turn()

        # when the selected move is invalid
        elif piece == None and (new_row, new_col) not in self.valid_moves:
            self.valid_moves = {} # reset valid moves
            print("Invalid move!")
            return True
        
        else:
            return False
        return True


    def change_turn(self):
        self.valid_moves = {} # reset the valid moves
        if self.turn == BLUE:
            self.turn = RED
        else:
            self.turn = BLUE
        return self.turn


    def draw_valid_moves(self, moves, color):
        for move in moves:
            row, col = move
            if color == BLUE:
                valid_color = PINK
            else:
                valid_color = GREEN
            pygame.draw.circle(self.win, valid_color,  (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 10)


    def winner(self):
        winner = None
        red_king = self.board.search_king(RED) 
        blue_king = self.board.search_king(BLUE)
        if red_king != None:
            red_dist = self.board.calculate_distance_to_corner(RED, red_king[0], red_king[1])
        else:
            red_dist = -1
        if blue_king != None:
            blue_dist = self.board.calculate_distance_to_corner(BLUE, blue_king[0], blue_king[1])
        else:
            blue_dist = -1

        # king reaching opponent corner
        if blue_dist == 0:
            winner = BLUE
        elif red_dist == 0:
            winner = RED

        # capturing opponent king
        if not blue_king:
            winner = RED
        elif not red_king:
            winner = BLUE

        return winner
    
    # So the AI will return the new board after his turn
    def get_board(self):
        return self.board
    
    # Returns the actual move that the AI decides to make
    def ai_move(self, board):
        self.board= board
        self.change_turn()

    