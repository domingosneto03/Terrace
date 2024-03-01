import pygame
from terraceGame.constants import *
from terraceGame.game import Game


FPS = 60 # frames per second

pygame.font.init() # just to be able to write in the pieces

pygame.display.set_caption('Terrace')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def Menu():
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

    elif mode=='3': #Will this mode have different difficulties?
        run= True
        WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Terrace (Computer VS Computer)')

    else:
        run=False
        WIN = None

    return WIN, run



def main():
    WIN, run = Menu()
    clock = pygame.time.Clock()
    game = Game(WIN)

    
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print("The Winner is:")
            if game.winner() == BLUE:
                print("BLUE")
            elif game.winner() == RED:
                print("RED")
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