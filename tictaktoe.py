def printBoad(xState,ystate):
    
    print(f"0 | 1 | 2 ")
    print(f"--|---|---")
    print(f"3 | 4 | 5 ")
    print(f"--|---|---")
    print(f"6 | 7 | 8 ")
    


if __name__=="__main__":
    xState=[0,0,0,0,0,0,0,0]
    yState=[0,0,0,0,0,0,0,0]
    turn=1  #1 for x and 0 for   
    print ("welcome to tik tok toe ")
    while(True):
        printBoad(xState,yState)
        if(turn==1):
           print ("X's  Chance")
           Value=int(input("please enter a value "))
           
           xState[Value]=1
    
        else:
            print ("X's  Chance")
            Value=int(input("please enter a value "))
            yState[Value]=0
       
        break    