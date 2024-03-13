import copy 

#Question 6
def load_dimacs(filename) :
    File = open(filename, 'r')
    x = File.read()
    Array1 = x.splitlines()
    Final = Array2 = []
    Array1.append(' ')
    Flag = False
    for i in range(1, len(Array1)) :
        if Flag == True :
            break
        Final.append(Array2)
        Array2 = []
        var = ''
        for j in Array1[i] :
            if j == 0 :
                break

            if j != ' '  :
                var = var + j 
            else :
                if var == '' :
                    Flag = True 
                    break
                
                Array2.append(int(var))
                var = ''    
            
            """
            if j != ' ' and j != '0':
                if j == '-' :
                    Flag = True 
                elif Flag :
                    Array2.append(int(j)*-1)
                    Flag = False   
                else : 
                    Array2.append(int(j))
                elif   
                """       
    Final.pop(0)
    return Final

#Question 7
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
                    pyys = 1
                     

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

#Question 8
def branching_sat_solve(clause_set, partial_assignment) :


    def branching(clause_set, SAT, literal, partial_assignment, x) :
        x += 1
        SAT1 = copy.deepcopy(SAT)
        if literal not in SAT1 and literal*-1 not in SAT1:
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
            next = branching(clause_setC, SAT1, clause_setC[0][0], partial_assignment, x)
            if next :
                return next 
            return branching(clause_setC, SAT1, clause_setC[0][0]*-1, partial_assignment, x)
        else :
            if x == len(partial_assignment) :
                return False
            return branching(clause_setC, SAT1, partial_assignment[x], partial_assignment, x)
        
    SAT = []
    if partial_assignment != [] :
        literal = partial_assignment[0]
    else :
        literal = clause_set[0][0]
    x = 0      


    resulting = branching(clause_set, SAT, literal, partial_assignment, x)
    if resulting != False :
        for i in clause_set :
            for j in i :
                if j not in resulting and j*-1 not in resulting :
                    resulting.append(j) 
    return resulting

#Question 9
def unit_propogate(clause_set) :
    done = False 
    i = -1
    while not done :
        i += 1
     
        
        if len(clause_set) != 0 and len(clause_set[i]) == 1 :
            literal = clause_set[i][0]
            clause_set.pop(i)
            if len(clause_set) == 0 :
                break
            propogated = False
            j = -1
            i = -1
            
            while not propogated :
                j += 1
                
                if literal in clause_set[j] :
                    clause_set.pop(j)
                    j -= 1
                elif literal*-1 in clause_set[j] :
                    clause_set[j].remove(literal*-1)
                    j = -1
                    
                else :
                    propogated = True 

        else :
            break
    return clause_set


#Question 10 
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
           
            if [] in clause_setCopy  :
                return False
            CurrentVar = clause_setCopy[varIndex1][varIndex2]
               
            if CurrentVar*-1 in clause_setCopy[i] :
                if len(clause_setCopy[varIndex1])-1 == varIndex2 :
                    varIndex2 = 0 
                    varIndex1 += 1
                
                    if varIndex1 == len(clause_setCopy) :
                        break 
                else :
                    varIndex2 += 1
 
            if len(clause_setCopy)-1  == i and CurrentVar*-1 not in clause_setCopy[i] :
                if CurrentVar not in satisfying and CurrentVar*-1 not in satisfying:
                    satisfying.append(CurrentVar)
                #poppintime
                poppinIndex = -1
                popped = False
                i = -1
                while not popped :
                    poppinIndex += 1
                    if poppinIndex == len(clause_setCopy) :
                        break
                    if CurrentVar in clause_setCopy[poppinIndex] :
                        clause_setCopy.pop(poppinIndex)
                        poppinIndex -= 1
                    if len(clause_setCopy) == 0 :  
                        satisfying.append(0)
                        return satisfying
        
                varIndex1 = 0
                varIndex2 = 0

            #if no more pops break loop
            
            l1 = len(clause_setCopy)-1
            l2 = len(clause_setCopy[l1])-1
            if varIndex1 == l1 and varIndex2 == l2 :
                break     
        
        return clause_setCopy

    
    def unit_propogate(clause_set, satisfying) :
        
        copiedclause_set = copy.deepcopy(clause_set)
        done = False 
        i = -1
        while not done :
            i += 1
           
        
            if len(copiedclause_set) != 0 and len(copiedclause_set[i]) == 1 :
                literal = copiedclause_set[i][0]
                if literal not in satisfying and literal*-1 not in satisfying:
                    satisfying.append(literal)
                copiedclause_set.pop(i)
                if len(copiedclause_set) == 0 :
                    break
                propogated = False
                j = -1
                i = -1
            
                while not propogated :
                    j += 1
                    
                    
                    if literal in copiedclause_set[j] :
                        copiedclause_set.pop(j)
                        j -= 1
                    elif literal*-1 in copiedclause_set[j] :
                        
                        copiedclause_set[j].remove(literal*-1)
                        if len(copiedclause_set[j]) == 0 :
                            return False  
                        j = -1
                    
                    if len(copiedclause_set)-1 == j:
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
        if literal not in SAT1 and literal*-1 not in SAT1:
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
            if clause_setCopy == False :
                return False 
            
            if clause_setCopy[-1] == 0 :
                clause_setCopy.pop()
                return clause_setCopy
            
            """
            clause_setC = pure_literal_elim(SAT1, clause_setC)
            print(clause_setC, 'C')
            if clause_setC == False :
                return False 
            if clause_setC[-1] == 0 :
                clause_setC.pop()
                return clause_setC
                """
            

            
            next = branching(clause_setCopy, SAT1, clause_setCopy[0][0], partial_assignment)
            if next :
                return next 
            return branching(clause_setCopy, SAT1, clause_setCopy[0][0]*-1, partial_assignment)
        else :
            partial_assignment.pop(0)
            return branching(clause_setCopy, SAT1, partial_assignment[0], partial_assignment)
        
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


