from copy import deepcopy
import pygame
from minimax.algorithm import minimax
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
            self.board.piece_used(piece, self.turn)
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
        red_king = self.board.red_king_pos 
        blue_king = self.board.blue_king_pos
        if red_king != (-1, -1):
            red_dist = self.board.calculate_distance_to_corner(RED, red_king[0], red_king[1])
        else:
            red_dist = -1
        if blue_king != (-1, -1):
            blue_dist = self.board.calculate_distance_to_corner(BLUE, blue_king[0], blue_king[1])
        else:
            blue_dist = -1

        # king reaching opponent corner
        if blue_dist == 0:
            winner = BLUE
        elif red_dist == 0:
            winner = RED

        # capturing opponent king
        if blue_king == (-1, -1):
            winner = RED
        elif red_king == (-1, -1):
            winner = BLUE

        return winner
    
    # So the AI will return the new board after his turn
    def get_board(self):
        return self.board
    
    # Returns the actual move that the AI decides to make
    def ai_move(self, board):
        self.board= board
        self.change_turn()

    def get_hint(self):
        best_score = float('-inf')
        best_move = None
        for piece in self.board.get_all_pieces(BLUE):  # Accessing get_all_pieces() from the board
            valid_moves = self.board.get_valid_moves(piece)
            for move in valid_moves.items():
                temp_board = deepcopy(self.board)
                temp_piece = temp_board.get_piece(piece.row, piece.col)
                score, _ = minimax(temp_board, 1, BLUE, self, float('-inf'), float('inf'))  # Adjust depth as needed
                if score > best_score:
                    best_score = score
                    best_move = (piece.row+1, piece.col+1, move[0][0]+1, move[0][1]+1)

        return best_move