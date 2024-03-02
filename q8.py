import copy 

def branching_sat_solve(clause_set, partial_assigmnet) :
    copied = copy.deepcopy(clause_set)
    
    
    def checker(copied, partial_assignment) :
        for i in partial_assigmnet :
            j = -1
            sugma = False
            
            while not sugma :
                j += 1
                if len(copied) == j :
                    sugma = True 
                    break 
               
                k = -1
                nutz = False

                while not nutz :
                    
                    k += 1
                    if len(copied[j]) == k :
                        nutz = True
                    else :    
                        if copied[j][k] == i :
                            print(j, 'j')
                            print('i', i)
                            copied.pop(j)
                            print(copied, 'ins')
                            j -= 1
                            if len(copied) == 0 :
                                return partial_assigmnet
                    
                        elif copied[j][k]*-1 == i :
                            copied[j].pop(k) 
                            k -= 1
                            if len(copied[j]) == 0 :
                                return 
                    print(copied)

        
        
        
        """
        for i in partial_assigmnet :
            print('i', i)
            
            for j in range(len(copied)) :
                
                for k in range(len(copied[j])) :
                    print(k)
                    print('j', j)
                    if i == copied[j][k] :
                        copied.pop(j)
                        print('1', copied)
                        
                    elif i == copied[j][k]*-1 :
                        copied[j].pop(k)
                        print('2', copied)
                        if len(copied[j]) == 0 :
                            return False
        """                    
                        
                        

        return copied  

    if partial_assigmnet != [] :
        potato = checker(copied, partial_assigmnet) 
        if potato != None :
            return partial_assigmnet
        else :
            return False 

    def branching(clause_set, SAT, Max, literal) :
        SAT1 = copy.deepcopy(SAT)
        SAT1.append(literal)
        clause = copy.deepcopy(clause_set)
        
        i = -1
        done = False 
        while not done :
            i += 1
            clen = len(clause)
            if i == clen :
                done = True 
                break 
            j = -1
            finished = False   
            while not finished :
                j += 1

                if j == len(clause[i]) :
                    finished = True 
                else :    
                    if clause[i][j] == literal :
                        clause.pop(i)
                        i -= 1
                        if len(clause) == 0 :
                            return SAT1
                        break
                    elif clause[i][j]*-1 == literal :
                        clause[i].pop(j)
                        j -= 1
                        if len(clause[i]) == 0 :
                            return 
                  



        """
        for i in range(len(clause)) :
            for j in range(len(clause[i])) :
                print(i)
                print(j)
                print(clause)
                if clause[i][j] == literal :
                    clause.pop(i)
                    
                
                elif clause[i][j]*-1 == literal :
                    clause[i].pop(j)
                    if len(clause) == 0 :
                        return SAT1
                     
                    
                    if len(clause[i]) == 0 :
                        return 
        """ 
        
        if literal == Max :
            return
        if literal > 0 :
            result = branching(clause, SAT1, Max, literal+1)
            if result :
                return result
            return branching(clause, SAT1, Max, (literal*-1)-1)
        elif literal < 0 :
            result = branching(clause, SAT1, Max, literal-1)
            if result :
                return result
            return branching(clause, SAT1, Max, (literal*-1)+1)

    SAT = [] 
    Max = 3  
    
        
    x = branching(clause_set, SAT, Max, 1)
    y = branching(clause_set, SAT, Max, -1)

    if x :
        return x 
    elif y :
        return y 
    else : 
        return False

partial_assignment = [1, -2, 3]
clause_set = [[1],[1,-1],[-1,-2],[-2,3]]

hm = branching_sat_solve(clause_set, partial_assignment)
print(hm)


         
                     







        



             
                        

                
