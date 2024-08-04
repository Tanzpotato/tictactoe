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
l = [" "," "," "," "," "," "," "," "," "," "," "]

board = '''
                  |         | 
            {}     |   {}     |   {}
        _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                  |         |
            {}     |   {}     |   {}
        _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                  |         |
            {}     |   {}     |   {}       
                  |         |           '''.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
                  

while True:
     P1 = input("Player 1 - Do you want to choose X or O : ")
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
               if i%2==0:
                    if [l[0] , l[1] , l[2]] == ["O","O","O"]:
                         print("P2 WINS !")
                         break
                            
                    elif [l[3] , l[4] , l[5]] == ["O","O","O"]:
                         print("P2 WINS !")
                         break
                                
                    elif [l[6] , l[7] , l[8]] == ["O","O","O"]:
                         print("P2 WINS !")
                         break

                    elif [l[0] , l[3] , l[6]] == ["O","O","O"]:
                         print("P2 WINS !")
                         break

                    elif [l[1] , l[4] , l[7]] == ["O","O","O"]:
                         print("P2 WINS !")
                         break
                    elif [l[2] , l[5] , l[8]] == ["O","O","O"]:
                         print("P2 WINS !")
                         break
                               
                              
                    elif [l[0] , l[4] , l[8]] == ["O","O","O"]:
                         print("P2 WINS !")
                         break
                                 

                    elif [l[2] , l[4] , l[6]] == ["O","O","O"]:
                         print("P2 WINS !")
                         break

                    while True:
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
                              board = '''
                                                  |         | 
                                             {}    |   {}     |   {}
                                        _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                                                  |         |
                                             {}    |   {}     |   {}
                                        _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                                                  |         |
                                             {}    |   {}     |   {}       
                                                  |         |           
                                                  '''.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])

                              print(board)
                              break
                         
          
               elif i%2!=0:
                    if [l[0] , l[1] , l[2]] == ["X","X","X"]:
                         print("P1 WINS !")
                         break
                            
                    elif [l[3] , l[4] , l[5]] == ["X","X","X"]:
                         print("P1 WINS !")
                         break
                                
                    elif [l[6] , l[7] , l[8]] == ["X","X","X"]:
                         print("P1 WINS !")
                         break
                    elif [l[0] , l[3] , l[6]] == ["X","X","X"]:
                         print("P1 WINS !")
                         break

                    elif [l[1] , l[4] , l[7]] == ["X","X","X"]:
                         print("P1 WINS !")
                         break
                    elif [l[2] , l[5] , l[8]] == ["X","X","X"]:
                         print("P1 WINS !")
                         break
                               
                              
                    elif [l[0] , l[4] , l[8]] == ["X","X","X"]:
                         print("P1 WINS !")
                         break
                                 

                    elif [l[2] , l[4] , l[6]] == ["X","X","X"]:
                         print("P1 WINS !")
                         break
               
            
                    while True:
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
                                   board = '''
                                                       |         | 
                                                  {}    |   {}     |   {}
                                             _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                                                       |         |
                                                  {}    |   {}     |   {}
                                             _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                                                       |         |
                                                  {}    |   {}     |   {}       
                                                       |         |           
                                                       '''.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
                                   print(board)
                                   break
          elif P1=="O":
               if i%2==0:
                    if [l[0] , l[1] , l[2]] == ["O","O","O"]:
                         print("P1 WINS !")
                         break
                            
                    elif [l[3] , l[4] , l[5]] == ["O","O","O"]:
                         print("P1 WINS !")
                         break
                                
                    elif [l[6] , l[7] , l[8]] == ["O","O","O"]:
                         print("P1 WINS !")
                         break
                    elif [l[0] , l[3] , l[6]] == ["O","O","O"]:
                         print("P1 WINS !")
                         break

                    elif [l[1] , l[4] , l[7]] == ["O","O","O"]:
                         print("P1 WINS !")
                         break
                    elif [l[2] , l[5] , l[8]] == ["O","O","O"]:
                         print("P1 WINS !")
                         break                        

                              
                    elif [l[0] , l[4] , l[8]] == ["O","O","O"]:
                         print("P1 WINS !")
                         break
                                 

                    elif [l[2] , l[4] , l[6]] == ["O","O","O"]:
                         print("P1 WINS !")
                         break
                    
                    while True:
                         num = int(input("P2 which square do you choose - "))
                         if l[num-1] == "X":
                              print("This tile position is occupied")
      
                    
                         elif l[num-1] == "O":
                              print("This tile position is occupied")
                         
                         else:
                              print("\n"*100)
                              l.pop(num-1)
                              l.insert(num-1,"X")
                              board = '''
                                                  |         | 
                                             {}    |   {}     |   {}
                                        _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                                                  |         |
                                             {}    |   {}     |   {}
                                        _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                                                  |         |
                                             {}    |   {}     |   {}       
                                                  |         |           
                                                  '''.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])

                              print(board)
                              break
               elif i%2!=0:
                    if [l[0] , l[1] , l[2]] == ["X","X","X"]:
                         print("P2 WINS !")
                         break
                            
                    elif [l[3] , l[4] , l[5]] == ["X","X","X"]:
                         print("P2 WINS !")
                         break
                                
                    elif [l[6] , l[7] , l[8]] == ["X","X","X"]:
                         print("P2 WINS !")
                         break
                    elif [l[0] , l[3] , l[6]] == ["X","X","X"]:
                         print("P2 WINS !")
                         break

                    elif [l[1] , l[4] , l[7]] == ["X","X","X"]:
                         print("P2 WINS !")
                         break
                    elif [l[2] , l[5] , l[8]] == ["X","X","X"]:
                         print("P2 WINS !")
                         break
                               
                              
                    elif [l[0] , l[4] , l[8]] == ["X","X","X"]:
                         print("P2 WINS !")
                         break
                                 

                    elif [l[2] , l[4] , l[6]] == ["X","X","X"]:
                         print("P2 WINS !")
                         break                    
                    while True:
                              num = int(input("P1 which square do you choose - "))
                              if l[num-1] == "X":
                                   print("This tile position is occupied")
                              
                              elif l[num-1] == "O":
                                   print("This tile position is occupied")
                                   
                              else:
                         
                                   print("\n"*100)
                                   l.pop(num-1)
                                   l.insert(num-1,"O")
                                   board = '''
                                                       |         | 
                                                  {}    |   {}     |   {}
                                             _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                                                       |         |
                                                  {}    |   {}     |   {}
                                             _ _ _ _ _ |_ _ _ _ _|_ _ _ _ _
                                                       |         |
                                                  {}    |   {}     |   {}       
                                                       |         |           
                                                       '''.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
                                   print(board)
                                   break
               
