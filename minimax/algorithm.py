from copy import deepcopy
import pygame

RED = (255,0,0)
BLUE = (0, 0, 255)

def minimax(position, depth, player, game, alpha, beta):
    if depth == 0 or game.winner() != None:
        return position.evaluate(), position

    #if player == RED:
    if player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, False, game, alpha, beta)[0] # in the recursive call, only maxEval is necessary
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

            # alpha-beta cuts    
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, BLUE, game):
            evaluation = minimax(move, depth-1, True, game, alpha, beta)[0] # in the recursive call, only minEval is necessary
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
            
            # alpha-beta cuts 
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        
        return minEval, best_move

    '''    
    # useful for Computer vs Computer
    else:
        if player:
            minEval = float('inf')
            best_move = None
            for move in get_all_moves(position, BLUE, game):
                evaluation = minimax(move, depth-1, False, game, alpha, beta)[0] # in the recursive call, only maxEval is necessary
                minEval = min(minEval, evaluation)
                if minEval == evaluation:
                    best_move = move
                
                # alpha-beta cuts 
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break

            return minEval, best_move
        else:
            maxEval = float('-inf')
            best_move = None
            for move in get_all_moves(position, RED, game):
                evaluation = minimax(move, depth-1, True, game, alpha, beta)[0] # in the recursive call, only minEval is necessary
                maxEval = max(maxEval, evaluation)
                if maxEval == evaluation:
                    best_move = move
                
                # alpha-beta cuts 
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            
            return maxEval, best_move
    '''


def simulate_move(piece, move, board, game):
    # move looks like this ((row, col), None/<Piece>))
    row = move[0][0]
    col = move[0][1]
    target = move[1]
    if target != None:
        board.remove(target)
        if target.get_color() != piece.get_color():
            board.calculate_pieces_captured(piece.get_color())

    board.move(piece, row, col) #simulate the move
    board.creativity(piece, piece.get_color())
    board.calculate_distance_to_king(piece.get_color(), row, col) # after simulation calculate the distance to the king
    if piece.get_king_verification():
        board.calculate_distance_to_corner(piece.get_color(), row, col) # after simulation calculate the king's distance to opposite corner

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move in valid_moves.items():
            #draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game)
            moves.append(new_board)
    
    return moves

'''
# for testing
def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw_board(game.win)
    game.draw_valid_moves(valid_moves.keys(), piece.get_color())
    pygame.display.update()
    pygame.time.delay(20)
'''
