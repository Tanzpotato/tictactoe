print( ''' each number on your keyboard corresponds to a square as shown
                  |         | 
             1    |    2    |    3
        _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                  |         |
             4    |    5    |    6
        _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                  |         |
             7    |    8    |    9       
                  |         |           ''')
l = [" "," "," "," "," "," "," "," "," "]

board = '''
                  |         | 
            {}     |   {}     |   {}
        _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                  |         |
            {}     |   {}     |   {}
        _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                  |         |
            {}     |   {}     |   {}       
                  |         |           '''

def win(l,X,P1):   
     if l[0] == l[1] == l[2] == X:
          return (P1 + " WINS !")
                                   
     elif l[3] == l[4] == l[5] == X:
          return (P1 + " WINS !")
                                          
     elif l[6] == l[7] == l[8] == X:
          return (P1 + " WINS !")

     elif l[0] == l[3] == l[6] == X:
          return (P1 + " WINS !")
          
     elif l[1] == l[4] == l[7] == X:
          return (P1 + " WINS !")
                              
     elif l[2] == l[5] == l[8] == X:
          return (P1 + " WINS !")
                                                                    
     elif l[0] == l[4] == l[8] == X:
          return (P1 + " WINS !")
                                      
     elif l[2] == l[4] == l[6] == X:
          return (P1 + " WINS !")
     else:
          return (" ")
                            
while True:
     P1 = input("Player 1 - Do you want to choose X or O : ").upper()
     if P1=="X":
          print("Player 1 goes first")
          break 
     elif P1=="O":
          print("Player 2 goes first")
          break 
     else:
          print("invalid element chosen ")
          continue 
                       
for i in range(0,9):
          if P1 =="X":
               P2 = "O"
               if i%2==0:
                    if win(l,"O","P2") == "P2 WINS !" :
                         break
                    while True:
                        try:
                            num = int(input("P1 which square do you choose - "))

                            if l[num-1] == "X":
                                print("This tile position is occupied")
                                continue
                            
                            elif l[num-1] == "O":
                                print("This tile position is occupied")
                                continue 
                        
                            else:
                                print("\n"*100)
                                l.pop(num-1)
                                l.insert(num-1,"X")
                                tictac  = board.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])

                                print(tictac)
                                print(win(l,"X","P1"))
                                break
                        except ValueError:
                             print("game left incomplete")
                         
               elif i%2!=0:
                    if win(l,"X","P1") == "P1 WINS !":
                         break                                
                    while True:
                        try:
                            num = int(input("P2 which square do you choose - "))

                            if l[num-1] == "X":
                                print("This tile position is occupied")
                                continue
                            
                            elif l[num-1] == "O":
                                print("This tile position is occupied")
                                continue 
                        
                            else:
                                print("\n"*100)
                                l.pop(num-1)
                                l.insert(num-1,"O")
                                tictac  = board.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
                                print(tictac)
                                print(win(l,"O","P2"))
                                break
                        except ValueError:
                             print("game left incomplete")
          if l.count("X")==5 and l.count("O")==4:
               if win(l,"O","P2")!= "P2 WINS !" and  win(l,"X","P1") !="P1 WINS !":
                    print("GAME TIED")    
          elif P1=="O":
               P2 = "X"
               if i%2==0:
                    if win(l,"O","P1") == "P1 WINS !":
                         break                    
                    while True:
                        try:
                            num = int(input("P2 which square do you choose - "))

                            if l[num-1] == "X":
                                print("This tile position is occupied")
                                continue
                            
                            elif l[num-1] == "O":
                                print("This tile position is occupied")
                                continue 
                        
                            else:
                                print("\n"*100)
                                l.pop(num-1)
                                l.insert(num-1,"X")
                                tictac  = board.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
                                print(tictac)
                                print(win(l,"X","P2"))
                                break
                        except ValueError:
                             print("game left incomplete")
                         
               elif i%2!=0:
                    if win(l,"X","P2") == "P2 WINS !":
                         break                
                    while True:
                        try:
                            num = int(input("P1 which square do you choose - "))

                            if l[num-1] == "X":
                                print("This tile position is occupied")
                                continue
                            
                            elif l[num-1] == "O":
                                print("This tile position is occupied")
                                continue 
                        
                            else:
                                print("\n"*100)
                                l.pop(num-1)
                                l.insert(num-1,"O")
                                tictac  = board.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
                                print(tictac)
                                print(win(l,"O","P1"))
                                break
                        except ValueError:
                             print("game left incomplete")
          if l.count("X")==5 and l.count("O")==4:
               if win(l,"O","P1")!= "P1 WINS !" and  win(l,"X","P2") !="P2 WINS !":
                    print("GAME TIED") 