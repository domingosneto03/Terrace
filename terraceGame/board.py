import pygame
from terraceGame.constants import *
from terraceGame.piece import Piece

class Board:
    def __init__(self):
        self.grid = []
        self.create_grid()
        self.create_pieces()

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
                color = COLOR_PATTERN2[row][col]
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
        return self.grid[row][col]