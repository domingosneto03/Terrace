import pygame
from terraceGame.constants import *
from terraceGame.game import Game
from minimax.algorithm import minimax

FPS = 60 # frames per second

pygame.font.init() # just to be able to write in the pieces

pygame.display.set_caption('Terrace')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def Menu():
    difficulty = '0'
    #Picking the mode
    print("Welcome to Terrace!!"+
          "\nChoose a mode:"+
          "\n\t 1. Player VS Player"+
          "\n\t 2. Player VS Computer"+
          "\n\t 3. Computer VS Computer")
    mode=input("Please choose 1 2 3 or Q to quit: ").strip().lower()
    
    #For wrong inputs
    while mode not in ['1', '2', '3', 'q']:
        mode = input("Please write a valid answer: ").strip().lower()
    
    if mode=='1':
        run= True
        WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Terrace (Player VS Player)')
    
    #Picking difficulty for computer
    elif mode=='2':
        print("Choose Computer's difficulty:"
          "\n\t 1. Easy"+
          "\n\t 2. Medium"+
          "\n\t 3. Hard")
        difficulty=input("Please choose 1 2 3 or Q to quit: ").strip().lower()
        
        #For wrong inputs
        while difficulty not in ['1', '2', '3', 'q']:
            difficulty=input("Please write a valid answer: ").strip().lower()

        if difficulty=='1':
            run=True
            WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #TODO: I'm guessing WIN will change depending on the mode and difficulty?
            pygame.display.set_caption('Terrace (Player VS Easy Computer)')
        elif difficulty=='2':
            run=True
            WIN = pygame.display.set_mode((WIDTH,HEIGHT))
            pygame.display.set_caption('Terrace (Player VS Medium Computer)')
        elif difficulty=='3':
            run=True
            WIN = pygame.display.set_mode((WIDTH,HEIGHT))
            pygame.display.set_caption('Terrace (Player VS Hard Computer)')
        else:
            run=False
            WIN= None

    elif mode=='3':
        run=True
        WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #TODO: I'm guessing WIN will change depending on the mode and difficulty?
        pygame.display.set_caption('Terrace (Computer vs Computer)')

    else:
        run=False
        WIN = None

    return mode, WIN, run, difficulty

# stats of the game to appear at the end - want to make a table with the statistics
def stats(game):
    print("The Winner is:")
    if game.winner() == BLUE:
        print("BLUE")
    elif game.winner() == RED:
        print("RED")

def main():
    mode, WIN, run, difficulty = Menu()
    clock = pygame.time.Clock()
    game = Game(WIN)

    
    while run:
        clock.tick(FPS)

        if(mode=='1'):
            if game.winner() != None: # to improve
                stats(game)
                run = False
                WIN = None

        elif (mode=='2'):
            if(difficulty=='1'):
                if game.winner() != None: # to improve
                    stats(game)
                    run = False
                    WIN = None
                if game.turn ==RED:
                    value, new_board = minimax(game.board, 1, RED, game)
                    game.ai_move(new_board)

            if(difficulty=='2'):
                if game.winner() != None: # to improve
                    stats(game)
                    run = False
                    WIN = None
                if game.turn ==RED:
                    value, new_board = minimax(game.board, 2, RED, game)
                    game.ai_move(new_board)

            if(difficulty=='3'):
                if game.winner() != None: # to improve
                    stats(game)
                    run = False
                    WIN = None
                if game.turn ==RED:
                    value, new_board = minimax(game.board, 3, RED, game)
                    game.ai_move(new_board)

        # needs a lot of work - not yet implemented
        elif(mode=='3'):
            if game.winner() != None: # to improve
                stats(game)
                run = False
                WIN = None

        for event in pygame.event.get():
            
            # turn off
            if event.type == pygame.QUIT:
                run = False

            # select with mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()