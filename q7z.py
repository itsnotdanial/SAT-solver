import copy
def simple_sat_solve(clause_set) :
    
    def tree(clause_set, assignment, Satis) :
        SAT2 = copy.deepcopy(Satis)
        SAT2.append(assignment)
        clause_setS = copy.deepcopy(clause_set)
        for i in range(len(clause_setS)) :
            for j in range(len(clause_setS[i])) :
                if assignment == clause_setS[i][j] :
                    clause_setS[i][j] = True 
                elif assignment*-1 ==  clause_setS[i][j] :
                    clause_setS[i][j] = False 

        finished = True 
        for k in clause_setS :
            if finished == False :
                break
            for p in k :
                if p == True or p == False :
                    print('cool') 

                else :
                    finished = False
                    assignment = p
                    break 

        if finished == True :
            for hmm in clause_setS :
                if True not in hmm :
                    return 
                elif clause_setS[len(clause_setS)-1] == hmm :
                    return SAT2
        else :
            leaf = tree(clause_setS, assignment, SAT2)
            if leaf :
                return leaf
            return tree(clause_setS, assignment, SAT2)
    Satis = []    
    val = tree(clause_set, clause_set[0][0], Satis)
    if val == None :
        return False 
    return val

clause_set = [[1, 2], [4], [4, 3, -3]]
app = simple_sat_solve(clause_set)
print(app)                   
                

    