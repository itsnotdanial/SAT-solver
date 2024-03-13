import copy



#clause_set = [[1, 2], [1, -3], [3, 4], [5, 6], [-5, -6]]
#clause_set = [[1, -2, 3], [-1, 2, -3]]
#clause_set = [[1, -2],[1, 2],[-1, -2], [-1, 2]]
clause_set = [[1],[1,-1],[-1,-2,-3],[-2],[6]]

def dpll_sat_solve(clause_set, partial_assignment) :
    
    
    
    
    def pure_literal_elim(satisfying, clause_setCopy) :
        #determine which literals occur the most 
        #identify the pure literals
        #eliminate them one by one 
        #loop through 
        #append the places there is a pure literal 
        #if there is no contradiction pop the clauses from the clause set 
        i = -1
        varIndex2 = 0
        varIndex1 = 0 
        elimmed = False
        while not elimmed :
            i += 1
            if i > len(clause_setCopy)-1 :
                break
            print(varIndex1, 'varIndex1')
            print(varIndex2, 'varIndex2')
            print(clause_setCopy, 'b4 var2')
            if clause_setCopy == [[]] :
                return False
            CurrentVar = clause_setCopy[varIndex1][varIndex2]
            print(CurrentVar, 'var')
            
            
            print(i, 'index') 
            print(clause_setCopy)   
            if CurrentVar*-1 in clause_setCopy[i] :
                if len(clause_setCopy[varIndex1])-1 == varIndex2 :
                    varIndex2 = 0 
                    varIndex1 += 1
                
                    if varIndex1 == len(clause_setCopy) :
                        break 
                else :
                    varIndex2 += 1
 
            if len(clause_setCopy)-1  == i and CurrentVar*-1 not in clause_setCopy[i] :
                satisfying.append(CurrentVar)
                #poppintime
                poppinIndex = -1
                popped = False
                i = -1
                while not popped :
                    poppinIndex += 1
                    if poppinIndex == len(clause_setCopy) :
                        break
                    print(poppinIndex, 'pop')
                    print(clause_setCopy)
                    if CurrentVar in clause_setCopy[poppinIndex] :
                        clause_setCopy.pop(poppinIndex)
                        poppinIndex -= 1
                        if len(clause_setCopy) == 0 :
                            print(clause_setCopy, 'clauseSetCopy')
                            satisfying.append(0)
                            return satisfying
        
                varIndex1 = 0
                varIndex2 = 0

            #if no more pops break loop
            l1 = len(clause_setCopy)-1
            l2 = len(clause_setCopy[l1])-1
            if CurrentVar == clause_setCopy[l1][l2] :
                break     
        
        return clause_setCopy

    
    def unit_propogate(clause_set, satisfying) :
        copiedclause_set = copy.deepcopy(clause_set)
        done = False 
        i = -1
        while not done :
            i += 1
            print(i)
            print(clause_set)
        
            if len(copiedclause_set) != 0 and len(copiedclause_set[i]) == 1 :
                literal = copiedclause_set[i][0]
                satisfying.append(literal)
                copiedclause_set.pop(i)
                if len(copiedclause_set) == 0 :
                    break
                propogated = False
                j = -1
                i = -1
            
                while not propogated :
                    j += 1
                    print(j)
                    print(copiedclause_set)
                    if literal in copiedclause_set[j] :
                        copiedclause_set.pop(j)
                        j -= 1
                    elif literal*-1 in copiedclause_set[j] :
                        copiedclause_set[j].remove(literal*-1)
                        j = -1
                    
                    else :
                        propogated = True 

            else :
                break
        if copiedclause_set != [] :   
            return copiedclause_set
        else :
            satisfying.append(0)
            return satisfying

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
            clause_setCopy = unit_propogate(clause_setC, SAT1)
            if clause_setCopy[-1] == 0 :
                clause_setCopy.pop()
                return clause_setCopy
            
            clause_setC = pure_literal_elim(SAT1, clause_setCopy)
            if clause_setC == False :
                return False 
            if clause_setC[-1] == 0 :
                clause_setC.pop()
                return clause_setC
            

            
            next = branching(clause_setC, SAT1, clause_setC[0][0], partial_assignment)
            if next :
                return next 
            return branching(clause_setC, SAT1, clause_setC[0][0]*-1, partial_assignment)
        else :
            partial_assignment.pop(0)
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



 
partial_assignment = []
hmm = dpll_sat_solve(clause_set, partial_assignment)
print(hmm)
   

                            

                

                            




                        





        




