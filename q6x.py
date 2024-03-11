def load_dimacs(filename) :
    File = open(filename, 'r')
    x = File.read()
    Array1 = x.splitlines()
    Final = Array2 = []
    Array1.append(' ')
    Flag = False
    for i in range(1, len(Array1)) :
        print(Array2)
        Final.append(Array2)
        Array2 = []
        for j in Array1[i] :
            print(j)
            if j != ' ' and j != '0' :
                if j == '-' :
                    Flag = True 
                elif Flag :
                    Array2.append(int(j)*-1)
                    Flag = False   
                else : 
                    Array2.append(int(j))     
    Final.pop(0)
    return Final

 