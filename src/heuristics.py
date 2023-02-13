def shannonHeuristic(b):
    def nb_symbol(s):
        n=0
        dict=b.piece_map()
        for i in dict:
            if dict[i].symbol() == s:
                n+=1
        return n
    def evaluatePawn(s):
        dict = b.piece_map()
        sum = 0
        for i in dict:
            if dict[i].symbol() == 'p' == s:
                sum+=((i//8)-1)*0.5
            if dict[i].symbol() == s == 'P':
                sum+=(((63-i)//8)-1)*0.5
        return sum
    return 200*(nb_symbol("K")-nb_symbol("k"))+9*(nb_symbol("Q")-nb_symbol("q"))+5*(nb_symbol("R")-nb_symbol("r"))+3*(nb_symbol("B")-nb_symbol("b")+nb_symbol("N")-nb_symbol("n"))+(nb_symbol("P")-nb_symbol("p")) + (evaluatePawn('P') - evaluatePawn('p'))

""" 
Add other heuristics
"""
