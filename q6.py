import re 

def load_dimacs() :
    Opened = open("test.txt", "r") 
    ReadArray = Opened.readlines()
    print('ReadArray', ReadArray)
    counter = 1 
    FinalArray = []

    for counter in range(1, len(ReadArray)) :
        TempArray = []
        ArrayLength = len(ReadArray[counter])
        ReadList = ReadArray[counter]
        print(ArrayLength)
        j = 0 

        
        while j < ArrayLength :
            
            print('xd ', ReadList[j])
            if  ReadList[j] == '0' :
                FinalArray.append(TempArray)
                print('This is FinalArray ', FinalArray)
                break
            
            


            elif ReadList[j] != ' ' :
                if ReadList[j] == '-' :
                    TempArray.append(int(ReadList[j]+ReadList[j+1]))
                    j = j + 1
                else :
                    print('TempArray ', TempArray)
                    TempArray.append(int(ReadList[j]))
                    print('TempArray2 ', TempArray)
            
            j = j + 1
        

    return FinalArray 
        

#x = load_dimacs()
#print('Potato ', x) 

def simple_sat_solve(clause_set) :
    

