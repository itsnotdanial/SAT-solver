import copy 
clause_set = [[1, -2], [-1, 2], [-1, -2], [1, 2]]

def simple_sat_solve(clause_set) :
    
    #branching tree
    def finish(clause_set) :
        
        Resolved = True 
        for i in clause_set :
            if True in i :
                print('cool')
            else :
                Resolved = False 
                break   
                

        return Resolved

    
    
    
    
    def branching(Max, CurrentVar, SAT, clause_set)  :
        clause_set1 = copy.deepcopy(clause_set)
        SAT1 = copy.deepcopy(SAT)
        
        SAT1.append(CurrentVar)
        for i in clause_set1 :
            for j in range(len(i)) :
                if i[j] == CurrentVar :
                    i[j] = True
                elif i[j] == CurrentVar*-1 :
                    i[j] = False 
        print('clause', clause_set1)                
        
        if CurrentVar == Max or CurrentVar*-1 == Max :
            lol = finish(clause_set1)
             
            if lol == True :
                print('SAT', SAT1)
                return SAT1
            else :
                print('Entering F')
                return None 
        
        

        if CurrentVar > 0 :
            result = branching(Max, CurrentVar+1, SAT1, clause_set1)
            if result :
                return result  
            return branching(Max, (CurrentVar*-1)-1, SAT1, clause_set1)
        else :
            
            result = branching(Max, CurrentVar-1, SAT1, clause_set1)
            if result :
                return result
            else :
                return branching(Max, (CurrentVar*-1)+1, SAT1, clause_set1) 

    Max = 2
    CurrentVar = 1
    SAT = []
    x = branching(Max, CurrentVar, SAT, clause_set)
    z = branching(Max, CurrentVar*-1, SAT, clause_set)
    print(x)
    print(z)
    if x != None :
        return x
    elif z != None :
        return z 
    else : 
        return False 

y = simple_sat_solve(clause_set) 
print(y)       

         





       