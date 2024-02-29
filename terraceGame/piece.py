import pygame
from terraceGame.constants import *


class Piece:
    def __init__(self, row, col, color, size, isKing):
        self.row = row
        self.col = col
        self.color = color
        self.size = size
        self.isKing = isKing
        self.center_x = 0
        self.center_y = 0
        self.calc_pos()
    
    # calculates the exact position the piece will be drawn
    def calc_pos(self):
        self.center_x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.center_y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    # piece outline
    def outline(size):
        if size == SIZE_BIG:
            return GREEN
        elif size == SIZE_MEDIUM:
            return YELLOW
        elif size == SIZE_SMALL:
            return PINK
        else:
            return ORANGE

    def draw(self, win):
        radius = (SQUARE_SIZE // 2 - 5) * self.size
        outline_color = Piece.outline(self.size)
        pygame.draw.circle(win, outline_color, (self.center_x, self.center_y), radius + 3, width=3)
        pygame.draw.circle(win, self.color, (self.center_x, self.center_y), radius)

        # Draw 'T' symbol
        if self.isKing == True:  # Only draw 'T' for King pieces
            font = pygame.font.Font(None, 25)
            text = font.render("T", True, WHITE)  # 'T' symbol color is green
            text_rect = text.get_rect(center=(self.center_x, self.center_y))
            win.blit(text, text_rect)
    
    # function to move the piece
    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col
        self.calc_pos()   
