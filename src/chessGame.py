import randomPlayer
import minimaxPlayer
import alphaBetaPlayer
import chess
import numpy as np

board = chess.Board()

"""
I will organize a game between mimimax player with prof 3 and random player a see the results    
                               mimimax player with prof 3 and minimax player with prof 1 a see the results    
                                                
"""
def game(b):
    i = 1
    while(not(b.is_game_over())):
        alphaBetaPlayer.playMove(b, -np.inf, np.inf, 3)
        print(alphaBetaPlayer.getPlayerName(), " prof 3: \n", b, "\n###########################\n")
        #b.push(randomPlayer.randomMove(b))
        #print("RandomPlayed played: \n", b, "\n###########################\n")
        minimaxPlayer.playMove(b, 3)
        print(minimaxPlayer.getPlayerName(), " prof 1: \n", b, "\n###########################\n")
        print("Iteration: ", i, "\n###########################\n")
        i+=1


if __name__ == '__main__':
    game(board)
