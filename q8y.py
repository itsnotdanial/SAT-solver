import copy

def branching_sat_solve(clause_set, partial_assignment) :


    def branching(clause_set, SAT, literal, partial_assignment) :
        SAT1 = copy.deepcopy(SAT)
        SAT1.append(literal)
        clause_setC = copy.deepcopy(clause_set)
        popping = True
        i = -1
        while popping :
            i += 1
            clen = len(clause_setC)
            if i == clen :
                break

            if literal in clause_setC[i] :
                clause_setC.pop(i)
                i -= 1
                clen -= 1
                if clen == 0 :
                    return SAT1
        
            elif literal*-1 in clause_setC[i] :
                clause_setC[i].remove(literal*-1)
                if len(clause_setC[i]) == 0 :
                    return False       
        if partial_assignment == [] :
            next = branching(clause_setC, SAT1, clause_setC[0][0], partial_assignment)
            if next :
                return next 
            return branching(clause_setC, SAT1, clause_setC[0][0]*-1, partial_assignment)
        else :
            partial_assignment.pop(0)
            print(partial_assignment)
            return branching(clause_setC, SAT1, partial_assignment[0], partial_assignment)
                
    SAT = []
    if partial_assignment != [] :
        literal = partial_assignment[0]
    else :
        literal = clause_set[0][0]
         


    resulting = branching(clause_set, SAT, literal, partial_assignment)
    if resulting != False :
        for i in clause_set :
            for j in i :
                if j not in resulting and j*-1 not in resulting :
                    resulting.append(j) 
    return resulting  

partial_assignment = [1, -2, 6]
clause_set = [[1],[1,-1],[-1,-2,-3],[-2],[6]]
oop = branching_sat_solve(clause_set, partial_assignment)
print(oop)








