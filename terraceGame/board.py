import pygame
from terraceGame.constants import *
from terraceGame.piece import Piece

class Board:
    def __init__(self):
        self.grid = []
        self.create_grid()
        self.create_pieces()
        self.red_left = self.blue_left = 16 # not entirely necessary, just for testing

    def create_grid(self):
        for row in range(ROWS):
            self.grid.append([])
            for col in range(COLS):
                self.grid[row].append(None)

    def create_pieces(self):
        for row in range(ROWS):
            for col in range(COLS):
                if row < 2:
                    # big red piece
                    if (row == 0 and col < 2) or (row == 1 and col >= COLS - 2):
                        self.grid[row][col] = Piece(row, col, RED, SIZE_BIG, False)

                    # medium red piece
                    elif (row == 0 and col >= 2 and col < 4) or (row == 1 and col >= 4 and col < 6):
                        self.grid[row][col] = Piece(row, col, RED, SIZE_MEDIUM, False)

                    # small red piece
                    elif (row == 0 and col >= 4 and col < 6) or (row == 1 and col >= 2 and col < 4):
                        self.grid[row][col] = Piece(row, col, RED, SIZE_SMALL, False)

                    # smaller red piece
                    elif (row == 0 and col == 6) or (row == 1 and col < 2):
                        self.grid[row][col] = Piece(row, col, RED, SIZE_SMALLER, False)
                    
                    # King red piece
                    else:
                        self.grid[row][col] = Piece(row, col, RED, SIZE_SMALLER, True)

                elif row >= ROWS - 2:
                    # big blue piece
                    if (row == 6 and col < 2) or (row == 7 and col >= COLS - 2):
                        self.grid[row][col] = Piece(row, col, BLUE, SIZE_BIG, False)

                    # medium blue piece
                    elif (row == 6 and col >= 2 and col < 4) or (row == 7 and col >= 4 and col < 6):
                        self.grid[row][col] = Piece(row, col, BLUE, SIZE_MEDIUM, False)

                    # small blue piece
                    elif (row == 6 and col >= 4 and col < 6) or (row == 7 and col >= 2 and col < 4):
                        self.grid[row][col] = Piece(row, col, BLUE, SIZE_SMALL, False)

                    # smaller blue piece
                    elif (row == 6 and col >= COLS - 2) or (row == 7 and col == 1):
                        self.grid[row][col] = Piece(row, col, BLUE, SIZE_SMALLER, False)
                    
                    # King blue piece
                    else:
                        self.grid[row][col] = Piece(row, col, BLUE, SIZE_SMALLER, True)
    
    def draw_board(self, win):
        win.fill(WHITE)

        for row in range(ROWS):
            for col in range(COLS):
                color = COLOR_PATTERN[row][col]
                pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.rect(win, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
                piece = self.grid[row][col]
                if piece:
                    piece.draw(win)
        
        # Draw the horizontal line to divide the two halfs
        pygame.draw.line(win, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 3)

    # switch coordinates on board with the move
    def move(self, piece, new_row, new_col):
        self.grid[piece.row][piece.col], self.grid[new_row][new_col] = self.grid[new_row][new_col], self.grid[piece.row][piece.col]
        piece.move(new_row, new_col)

    # method to get the piece
    def get_piece(self, row, col):
        position =  self.grid[row][col]
        if position is None:
            return 0
        else:
            return self.grid[row][col]
    
    # method o reomove a piece from the board
    def remove(self, piece):
        if piece.get_color() == BLUE:
            self.blue_left = self.blue_left - 1
        else:
            self.red_left = self.red_left - 1
            
        self.grid[piece.row][piece.col] = None

    # method to get the valid moves
    def get_valid_moves(self, piece):
        moves = {}
        current_level = COLOR_PATTERN[piece.row][piece.col]

        # Check empty squares on the same level
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) != (piece.row, piece.col):
                    target_piece = self.grid[row][col]
                    target_level = COLOR_PATTERN[row][col]

                    # moving in the same level
                    if target_level == current_level:
                        if target_piece is None:
                            moves[(row, col)] = target_piece

                    # moving in a different level
                    else:
                        if self.cross_center(current_level, target_level) == False:    
                            # moving to a higher level
                            if self.higher_level(current_level, target_level, piece.row, piece.col, row, col) == target_level:
                                row_dir, col_dir = row - piece.row, col - piece.col
                                if target_piece is None:
                                    # can move either in straight or diagonal direction
                                    if (abs(row_dir) == 1 and col_dir == 0) or (row_dir == 0 and abs(col_dir) == 1) or (abs(row_dir) == 1 and abs(col_dir) == 1): # check if moves only 1 square
                                        moves[(row, col)] = target_piece

                            # moving to a lower level
                            else:
                                # can only move in a straight direction
                                if target_piece is None:
                                    row_dir, col_dir = row - piece.row, col - piece.col
                                    if (abs(row_dir) == 1 and col_dir == 0) or (row_dir == 0 and abs(col_dir) == 1): # check if moves only 1 square
                                            moves[(row, col)] = target_piece
                                else:
                                    row_dir, col_dir = row - piece.row, col - piece.col
                                    # check if it is the opponet's piece
                                    if piece.get_color() != target_piece.get_color():
                                        # can capture if the piece is bigger or equal than the opponent and if the direction is diagonal
                                        if (abs(row_dir) == 1 and abs(col_dir) == 1) and (piece.get_size() >= target_piece.get_size()): # check if moves only 1 square
                                            moves[(row, col)] = target_piece

        return moves
    

    def get_all_pieces(self,color):
        pieces= []
        for row in self.grid:
            for piece in row:
                if piece!=0 and piece.get_color()==color:
                    pieces.append(piece)
        return pieces
    


    # method to check which level is higher - super complicated and confusing, don't even try to follow
    def higher_level(self, current_level, target_level, current_row, current_col, target_row, target_col):
        if current_row < 4:
            if current_col < 4: 
                if current_row > target_row:
                    return target_level
                elif current_row < target_row:
                    return current_level
                else:
                    if current_col > target_col:
                        return target_level
                    else:
                        return current_level
            else:
                if current_col > target_col:
                    return target_level
                elif current_col < target_col:
                    return current_level
                else:
                    if current_row > target_row:
                        return target_level
                    else:
                        return current_level
        else:
            if current_col < 4: 
                if current_col > target_col:
                    return current_level
                elif current_col < target_col:
                    return target_level
                else:
                    if current_row > target_row:
                        return target_level
                    else:
                        return current_level
            else:
                if current_row > target_row:
                    return current_level
                elif current_row < target_row:
                    return target_level
                else:
                    if current_col > target_col:
                        return current_level
                    else:
                        return target_level

    # method to check if the move is across the center
    def cross_center(self, current_level, target_level):
        if current_level == LIGHT_GREY2 and target_level == LIGHT_GREY7:
            return True
        if current_level == LIGHT_GREY7 and target_level == LIGHT_GREY2:
            return True
        if current_level == GREY5 and target_level == GREY3:
            return True
        if current_level == GREY3 and target_level == GREY5:
            return True
        return False
    

    def evaluate(self):
        return self.blue_left - self.red_left