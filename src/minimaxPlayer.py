import numpy as np
import heuristics

def getPlayerName():
    return "Minimax player"

######################################################################

def MaxMin(b, profondeur):
    if b.is_game_over() or profondeur == 0:
        return heuristics.shannonHeuristic(b)
    meilleur = -np.inf
    for x in b.generate_legal_moves():
        b.push(x)
        meilleur = max(meilleur, MinMax(b, profondeur-1))  
        b.pop()
    return meilleur


def MinMax(b, profondeur):
    if b.is_game_over() or profondeur == 0:
        return heuristics.shannonHeuristic(b)
    pire = np.inf
    for x in b.generate_legal_moves():
        b.push(x)
        pire = min(pire, MaxMin(b, profondeur-1))
        b.pop()
    return pire

######################################################################

def ExtractMoves(b, profondeur):
    res = []
    for x in b.generate_legal_moves():
        b.push(x)
        res.append([x])
        b.pop()
    for y in res:
        b.push(y[0])
        y.append(MaxMin(b, profondeur-1))
        b.pop()
    return res
   
import random
   
def playMove(b, profondeur):
    possible_moves = ExtractMoves(b, profondeur)
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
    #print("I played this move: (score = ", best_score, ")\n")
    #print(b)
