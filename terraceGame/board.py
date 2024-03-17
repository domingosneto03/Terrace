import pygame
import math
from terraceGame.constants import *
from terraceGame.piece import Piece

class Board:
    def __init__(self):
        self.grid = []
        self.create_grid()
        self.create_pieces()

        self.red_count = 16
        self.blue_count = 16

        # calculated with hypotenuse
        self.dist_to_blue_king = 10
        self.dist_to_red_king = 10

        # initial distance is hypotenuse of the board
        self.blue_dist_to_red_corner = round(math.sqrt(math.pow(7, 2) + math.pow(7, 2)))
        self.red_dist_to_blue_corner = round(math.sqrt(math.pow(7, 2) + math.pow(7, 2)))

        # list of pieces and respective number of times used -> contained by lists that store the piece object and number of times used
        self.blue_used_pieces = []
        self.red_used_pieces = []
        self.store_all_pieces()


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


    # method that stores all pieces and respective times used in a list
    def store_all_pieces(self):
        for row in self.grid:
            for piece in row:
                if piece != None:
                    if piece.get_color() == RED:
                        self.red_used_pieces.append([piece, 0])
                    else:
                        self.blue_used_pieces.append([piece, 0])


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
        pygame.draw.line(win, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 3) # Draw the horizontal line to divide the two halfs


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


    # method o remove a piece from the board
    def remove(self, piece):
        self.grid[piece.row][piece.col] = None
        if piece.get_color() == BLUE:
            self.blue_count -= 1
        else:
            self.red_count -= 1


    # method to calculate a distance of a piece to the opponent's king
    # logic: Pythagorean theorem
    # calculate the number of rows (leg1) and columns (leg2) left to reach the king piece and determine the distance (hypotenuse)
    def calculate_distance_to_king(self, color, piece_row, piece_col):
        if color == RED:
            if self.search_king(BLUE):
                king_row, king_col = self.search_king(BLUE)
                if piece_row == king_row:
                    self.dist_to_blue_king = abs(piece_col - king_col) # if the king is in the same row
                elif piece_col == king_col:
                    self.dist_to_blue_king = abs(piece_row - king_row) # if the king is in the same row
                else:
                    leg1 = abs(piece_row - king_row)
                    leg2 = abs(piece_col - king_col)
                    self.dist_to_blue_king = round(math.sqrt(math.pow(leg1, 2) + math.pow(leg2, 2))) # distance is rounded to unit
        else:
            if self.search_king(RED):
                king_row, king_col = self.search_king(RED)
                if piece_row == king_row:
                    self.dist_to_red_king = abs(piece_col - king_col) # if the king is in the same row
                elif piece_col == king_col:
                    self.dist_to_red_king = abs(piece_row - king_row) # if the king is in the same row
                else:
                    leg1 = abs(piece_row - king_row)
                    leg2 = abs(piece_col - king_col)
                    self.dist_to_red_king = round(math.sqrt(math.pow(leg1, 2) + math.pow(leg2, 2))) # distance is rounded to unit


    # method to calculate a distance of the king to the opponent's opposite corner
    # logic: Pythagorean theorem
    # calculate the number of rows (leg1) and columns (leg2) left to reach the king piece and determine the distance (hypotenuse)
    def calculate_distance_to_corner(self, piece_color, piece_row, piece_col):

        # (row, col)
        red_corner = (0, 7)
        blue_corner = (7, 0)

        if piece_color == RED:

            # if the king is in the same row as the corner
            if piece_row == blue_corner[0] and piece_col != blue_corner[1]:
                self.red_dist_to_blue_corner = abs(piece_col - blue_corner[1])

            # if the king is in the same row as the corner    
            elif piece_col == blue_corner[1] and piece_row != blue_corner[0]:
                self.red_dist_to_blue_corner = abs(piece_row - blue_corner[0])

            # if the king is in the corner
            elif piece_row == blue_corner[0] and piece_col == blue_corner[1]:
                self.red_dist_to_blue_corner = 0

            else:
                leg1 = abs(piece_row - blue_corner[0])
                leg2 = abs(piece_col - blue_corner[1])
                self.red_dist_to_blue_corner = round(math.sqrt(math.pow(leg1, 2) + math.pow(leg2, 2))) # distance is rounded to unit
            
            return self.red_dist_to_blue_corner
        
        else:
            # if the king is in the same row as the corner
            if piece_row == red_corner[0] and piece_col != red_corner[1]:
                self.blue_dist_to_red_corner = abs(piece_col - red_corner[1])
            
            # if the king is in the same row as the corner
            elif piece_col == red_corner[1] and piece_col != red_corner[1]:
                self.blue_dist_to_red_corner = abs(piece_row - red_corner[0])
            
            # if the king is in the corner
            elif piece_row == red_corner[0] and piece_col == red_corner[1]:
                self.blue_dist_to_red_corner = 0

            else:
                leg1 = abs(piece_row - red_corner[0])
                leg2 = abs(piece_col - red_corner[1])
                self.blue_dist_to_red_corner = round(math.sqrt(math.pow(leg1, 2) + math.pow(leg2, 2))) # distance is rounded to unit
            
            return self.blue_dist_to_red_corner


    # method to loop through the board and find the king
    def search_king(self, color):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.grid[row][col]
                if piece != None:
                    if piece.get_king_verification():
                        if piece.get_color() == color:
                            return row, col
        if color == RED:
            self.red_king = False
        else:
            self.blue_king = False
    
    # method to check if a piece is being used repeatedly or not -> improve with list
    def creativity(self, piece, color):

        # red pieces
        if color == RED:
            for red_piece in self.red_used_pieces:
                if red_piece[0] == piece:
                    red_piece[1] += 1

        # blue pieces
        else:
            for blue_piece in self.blue_used_pieces:
                if blue_piece[0] == piece:
                    blue_piece[1] += 1

    # method to get the valid moves for a piece
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
                        if not self.cross_center(current_level, target_level):    
                            # moving to a higher level
                            if self.higher_level(piece.row, piece.col, row, col):
                                row_dir, col_dir = row - piece.row, col - piece.col
                                if target_piece is None:
                                    # can move either in straight or diagonal direction
                                    if (abs(row_dir) == 1 and col_dir == 0) or (row_dir == 0 and abs(col_dir) == 1) or (abs(row_dir) == 1 and abs(col_dir) == 1): # check if moves only 1 square
                                        moves[(row, col)] = target_piece

                            # moving to a lower level
                            elif not self.higher_level(piece.row, piece.col, row, col):
                                # can only move in a straight direction
                                if target_piece is None:
                                    row_dir, col_dir = row - piece.row, col - piece.col
                                    if (abs(row_dir) == 1 and col_dir == 0) or (row_dir == 0 and abs(col_dir) == 1): # check if moves only 1 square
                                            moves[(row, col)] = target_piece
                                else:
                                    row_dir, col_dir = row - piece.row, col - piece.col
                                    # can capture if the piece is bigger or equal than the opponent and if the direction is diagonal
                                    # cannibalism: can capture pieces from the same team for strategy matters
                                    if not (target_piece.get_king_verification() and piece.get_color() == target_piece.get_color()): # no suicides allowed
                                        if (abs(row_dir) == 1 and abs(col_dir) == 1) and (piece.get_size() >= target_piece.get_size()): # check if moves only 1 square
                                            moves[(row, col)] = target_piece
        return moves


    # method to check which level is higher - returns True if it is the target level, False otherwise
    def higher_level(self, current_row, current_col, target_row, target_col):
        current_level = BOARD_LEVEL_PATTERN[current_row][current_col]
        target_level = BOARD_LEVEL_PATTERN[target_row][target_col]
        if target_level > current_level: # moving to higher level
            return True 
        elif target_level < current_level: # moving to lower level
            return False
        else:
            return -1 # in case they are different planes but in the same level - not useful for the program


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
    
    # function to return all pieces
    def get_all_pieces(self,color):
        pieces= []
        for row in self.grid:
            for piece in row:
                if piece!=None and piece.get_color()==color:
                    pieces.append(piece)
        return pieces
    

    # function should return a score
    # highest score -> best move for RED
    # lowest score -> best move for BLUE
    # always a diff between red and blue team
    # multiplying by a value has an impact on the score, according to strategy need
    def evaluate(self):

        # evaluates how far is the piece of the opposite -> winning condition
        red_evaluation1 = -self.dist_to_blue_king * 1 # negative values to represent that the higher the distance, the lower the score
        blue_evaluation1 = self.dist_to_red_king * 1

        # evaluates how far is the king from the opposite corner -> winning condition
        red_evaluation2 = -self.red_dist_to_blue_corner * 3 # negative values to represent that the higher the distance, the lower the score
        blue_evaluation2 = self.blue_dist_to_red_corner * 3

        # evaluates who has more pieces
        red_evaluation3 = self.red_count * 20
        blue_evaluation3 = -self.blue_count * 20

        # evaluates if the AI is being diversive with the choice of its pieces
        red_evaluation4 = 0
        blue_evaluation4 = 0
        unique_red_counts = set()
        unique_blue_counts = set()
        for piece in self.red_used_pieces:
            count = piece[1] # number of times piece was used
            if count > 2:
                unique_red_counts.add(count) # set is used to avoid duplicate values
        for piece in self.blue_used_pieces:
            count = piece[1]
            if count > 2:
                unique_blue_counts.add(count)
        red_evaluation4 = -sum(unique_red_counts) * 1
        blue_evaluation4 = sum(unique_blue_counts) * 1

        if self.red_count - self.blue_count < 3:
            evaluation = red_evaluation3 + red_evaluation4 + blue_evaluation3 + blue_evaluation4
        else:
            evaluation = red_evaluation1 + red_evaluation2 + red_evaluation3 + blue_evaluation1 + blue_evaluation2 + blue_evaluation3
        
        return evaluation
    
        