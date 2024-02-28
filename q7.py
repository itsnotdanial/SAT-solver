clause_set = [[1, -2], [-1, 3]]

def simple_sat_solve(clause_set) : 
   #Directional Resolution
    biggest = 0
    for i in clause_set :
        for j in i :
            print(j)
            if abs(j) > biggest :
                biggest = j


    Bins = []
    for i in range(biggest) :
        Bins.append([])

    p = -1
    done = False
    LenC = len(clause_set)
    while not done :
        
        
        if p != -1 :
            print(temp)
            minimum = min(temp)-1
            print('m', minimum)
            print(Bins)
            Bins[minimum].append(clause_set[p])
        temp = []    
        p += 1  

        if p == LenC :
            break

        for k in clause_set[p] :
            print('x', k)
            temp.append(abs(k))
    

    #Now need to resolve
      

        

        

                




