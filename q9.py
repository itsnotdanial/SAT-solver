clause_set = [[1],[-1,2]]

def unit_propogate(clause_set) :
    done = False 
    i = -1
    while not done :
        i += 1
        print(i)
        print(clause_set)
        
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
                print(j)
                print(clause_set)
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


lol = unit_propogate(clause_set)      
print(lol)          