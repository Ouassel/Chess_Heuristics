import numpy as np
import heuristics

def getPlayerName():
    return "Alpha-Beta player"

######################################################################

def maxValue(b, alpha, beta, profondeur):
    if b.is_game_over() or profondeur == 0:
        return heuristics.shannonHeuristic(b)
    for x in b.generate_legal_moves():
        b.push(x)
        alpha = max(alpha, minValue(b, alpha, beta, profondeur-1))
        b.pop()
        if alpha >= beta: # prune
           return beta
    return alpha 

def minValue(b, alpha, beta, profondeur):
    if b.is_game_over() or profondeur == 0:
        return heuristics.shannonHeuristic(b)
    for x in b.generate_legal_moves():
        b.push(x)
        beta = min(beta, maxValue(b, alpha, beta, profondeur-1))
        b.pop()
        if alpha >= beta: # prune
           return alpha
    return beta

######################################################################

def ExtractMoves(b, alpha, beta, profondeur):
    res = []
    for x in b.generate_legal_moves():
        b.push(x)
        res.append([x])
        b.pop()
    for y in res:
        b.push(y[0])
        y.append(maxValue(b, alpha, beta, profondeur-1))
        b.pop()
    return res
   
import random
   
def playMove(b, alpha, beta, profondeur):
    possible_moves = ExtractMoves(b, alpha, beta, profondeur)
    print(possible_moves)
    store = []
    best_score = possible_moves[0][1]
    best_move = possible_moves[0]
    for x in possible_moves:
        if best_score < x[1]:
            best_score = x[1]
            best_move = x
            store.clear()
            store.append(best_move)
        elif best_score == x[1]:
            store.append(best_move)
    b.push(random.choice(store)[0])
