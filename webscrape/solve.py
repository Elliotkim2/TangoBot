from board import TangoBoard
import board
from copy import deepcopy
def error_check(board):
    for i, row in enumerate(board.grid):
        s_count = board.get_row_count("S",i)
        m_count = board.get_row_count("M",i)
        if s_count>3:
            
            print(f"too many S on row {i}")
            return True
        elif m_count>3:
            print(f"too many M on row {i}")
            return True
    return False
def undo(board, i, j):
    board.grid[i][j] = 'E'



def solved(board):
    
    new = deepcopy(board)

    while not new.complete():
        
        updated = False  # Tracks whether changes are made in the current iteration
        error = False
        for i, row in enumerate(new.grid):  # Iterate over all cells
            
            
            inrow = {'M': 0, 'S':0}
            for j, col in enumerate(row):
                print (j<=3 and new.grid[i][j+1] == new.grid[i][j+2] and new.grid[i][j+1] != 'E')
                
                col_inrow= {'M': 0, 'S':0}
                column = new.get_column(j)
                for s, ele in enumerate(column):
                    
                    
                    if new.grid[s][j] == "M":
                     
                        col_inrow["M"]+=1
                        col_inrow["S"]=0
        
                    elif new.grid[s][j] == "S":
                        col_inrow["S"]+=1
                        col_inrow["M"]=0

                    if new.grid[s][j] != "E":
                        
                        if new.crosses[j+s*6]:
                           
                            for num in new.crosses[j+s*6]:
                                if new.grid[num//6][num%6] == "E":
                                    if new.grid[s][j] == "M" :
                                        new.grid[num//6][num%6] = "S"
                                        if error_check(new):
                                            undo(new,num//6,num%6)
                                            print("1_cross")

                                        updated = True
                                 
                                        
                                        # if j == num%6:
                                        # #     print("H")
                                        # #     c_s_count+=1
                                        #     col_inrow["S"] = 1
                                        #     col_inrow["M"] = 0
                                    elif new.grid[s][j] == "S":
                                        
                                        new.grid[num//6][num%6] = "M"
                                        updated = True
                                        if error_check(new):
                                            undo(new,num//6,num%6)
                                            print(f"2_cross {s,j}")
                                    # if j == num%6:
                                    # #     print("H")
                                    # #     c_m_count+=1
                                    #     col_inrow["M"] = 1
                                    #     col_inrow["S"] = 0
                                    
                        if new.equals[j+s*6]:
                            for num in new.equals[j+s*6]: 
                                if new.grid[num//6][num%6] == "E":
                                    new.grid[num//6][num%6]=new.grid[s][j]
                                    updated = True
                                    if error_check(new):
                                        undo(new,num//6,num%6)
                                        print("3_equals")
                                # if j == num%6:
                                #     print("H")
                                #     col_inrow[new.grid[s][j]] += 1
                                    # if new.grid[s][j] == "M":
                                    #     print("H")
                                    #     # c_m_count+=1
                                    # else:
                                    #     # c_s_count+=1
                                    #     print("e")
                                    
                    elif new.grid[s][j] == "E":
                        c_m_count = new.get_col_count("M",j)
                        c_s_count = new.get_col_count("S",j)
                        
                        if c_m_count == 3:
                            new.grid[s][j] = "S"
                            if error_check(new):
                                print("4col_inrowS")
                                undo(new,s,j)
                            updated = True
                        elif c_s_count == 3:
                            new.grid[s][j] ="M"
                            if error_check(new):
                                print("5cscount 3")
                                undo(new,s,j)
                            updated = True
                        elif col_inrow["M"] == 2:
                            new.grid[s][j] = "S"
                            if error_check(new):
                                print("6col_inrowm")
                                undo(new,s,j)
                            else:
                                col_inrow["M"] = 0
                                col_inrow["S"] = 1
                            updated = True
                            # c_s_count +=1
                        elif col_inrow["S"] == 2:
                            new.grid[s][j] = "M"
                            if error_check(new):
                                print("7col_inrowS")
                                undo(new,s,j)
                            else:
                                col_inrow["M"] = 1
                                col_inrow["S"] = 0
                            updated = True
            
                        elif col_inrow["M"] == 1 and s<=4 and new.grid[s+1][j] == "M":
                            new.grid[s][j] = "S"
                            if error_check(new):
                                undo(new,s,j)
                                print("13_norm")
                            else:
                                col_inrow["S"] = 1
                                col_inrow["M"]= 0
                            updated = True
                            # c_s_count+=1
                            

                        elif col_inrow["S"] == 1 and s<=4 and new.grid[s+1][j] == "S":
                            new.grid[s][j] = "M"
                            if error_check(new):
                                undo(new,s,j)
                                print("14_norm")
                            else:
                                col_inrow["M"] = 1
                                col_inrow["S"]= 0
                            updated = True
                            # c_m_count+=1
                        elif s<=3 and new.grid[s+1][j] == new.grid[s+2][j]:
                            if new.grid[s+1][j] == "M":
                                new.grid[s][j] = "S"
                                if error_check(new):
                                    print("15_norm")
                                    undo(new,s,j)
                                # c_s_count+=1
                                else:
                                    col_inrow["S"]+=1
                                    col_inrow["M"] = 0
                            elif new.grid[s+1][j] == "S":
                                new.grid[s][j] = "M"
                                if error_check(new):
                                    print("16_norm")
                                    undo(new,s,j)
                                else:
                                # c_m_count+=1
                                    col_inrow["M"]+=1
                                    col_inrow["S"] = 0
                        if new.crosses[j+s*6]:
                            for num in new.crosses[j+s*6]:
                                if new.grid[num//6][num%6] != "E":
                                    if new.grid[num//6][num%6] == 'M':
                                        new.grid[s][j] = 'S'
                                        
                                    elif new.grid[num//6][num%6] == 'S':
                                        new.grid[s][j] = 'M'
                                    if error_check(new):
                                            undo(new,s,j)
                                            undo(new,num//6,num%6)
                                            print("8cross")
                                    else:
                                        if new.grid[num//6][num%6] == 'M':
                                            col_inrow["S"] += 1
                                            col_inrow["M"] = 0
                                        elif new.grid[num//6][num%6] == 'S':
                                            col_inrow["M"] += 1
                                            col_inrow["S"] = 0
                                    

                        if new.equals[j+s*6]:
                            for num in new.equals[j+s*6]: 
                                print(num)
                                if j == num%6 and new.grid[num//6][num%6] == "E":
                                    if c_m_count >= 2:
                                        new.grid[s][j] = "S"

                                        new.grid[num//6][num%6]="S"
                                        if error_check(new):
                                            undo(new,num//6,num%6)
                                            undo(new,s,j)
                                            print("9_equals")
                                        else:
                                            col_inrow["S"]+=1
                                            col_inrow["M"]=0
                                        updated = True
                                        # c_s_count+=2
                                    elif c_s_count >= 2:
                                        new.grid[s][j] = "M"
          
                                        new.grid[num//6][num%6]="M"
                                        if error_check(new):
                                            undo(new,num//6,num%6)
                                            undo(new,s,j)
                                            print("10_equals")
                                        else:
                                            col_inrow["M"]+=1
                                            col_inrow["S"]=0
                                        updated = True
                                        # c_m_count+=2
                                    elif col_inrow["M"]>=1:
                                        new.grid[s][j] = "S"
                                        
                                        new.grid[num//6][num%6]="S"
                                        if error_check(new):
                                            undo(new,num//6,num%6)
                                            undo(new,s,j)
                                            print("11_equals")
                                       
                                        else:
                                            col_inrow["S"]+=1
                                            col_inrow["M"]=0
                                        updated = True
                                        # c_s_count+=2
                                    elif col_inrow["S"]>=1:
                                        new.grid[s][j] = "M"
                                        
                                        new.grid[num//6][num%6]="M"
                                        if error_check(new):
                                            print("12_equals")
                                            undo(new,s,j)
                                            undo(new,num//6,num%6)
                                        else:
                                            col_inrow["M"]+=1
                                            col_inrow["S"]=0
                                        updated = True

                if new.grid[i][j] == "M":
                    
                    inrow["M"]+=1
                    inrow["S"]=0
    
                elif new.grid[i][j] == "S":
                    
                    inrow["S"]+=1
                    inrow["M"]=0

                elif new.grid[i][j] != "E":
                    if new.crosses[j+i*6]:
                        for num in new.crosses[j+i*6]:
                            if new.grid[num//6][num%6] == "E":
                                if new.grid[i][j] == "M":
                                    new.grid[num//6][num%6] = "S"
                                    if error_check(new):
                                        print("17_cross")
                                        undo(new,num//6,num%6)
                                    updated = True
                                    
                                    # if i == num//6:
                                    #     # r_s_count+=1
                                    #     inrow["S"] = 1
                                    #     inrow["M"] = 0
                                elif new.grid[i][j] == "S":
                                    new.grid[num//6][num%6] = "M"
                                    if error_check(new):
                                        print("18_cross")
                                        undo(new,num//6,num%6)
                                    updated = True
                                # if i == num//6:
                                #     # r_m_count+=1
                                #     inrow["M"] = 1
                                #     inrow["S"] = 0
                                
                    if new.equals[j+i*6]:
                        for num in new.equals[j+i*6]: 
                            if new.grid[num//6][num%6] == "E":
                                new.grid[num//6][num%6]=new.grid[i][j]
                                if error_check(new):
                                    print("19_euals")
                                    undo(new,num//6,num%6)
                                updated = True
                            # if i == num//6:
                            #     inrow[new.grid[i][j]] += 1
                                # if new.grid[i][j] == "M":
                                #     # r_m_count+=1
                                # else:
                                #     r_s_count+=1
                                
                elif new.grid[i][j] == "E":
                    r_m_count = new.get_row_count("M",i)
                    r_s_count= new.get_row_count("S",i)
                    if r_m_count == 3:
                        new.grid[i][j] = "S"
                        if error_check(new):
                            print("20_start")
                            undo(new,i,j)
                        updated = True


                    elif r_s_count == 3:
                        new.grid[i][j] ="M"
                        if error_check(new):
                            print("21_start")
                            undo(new,i,j)
                        updated = True
                    elif inrow["M"] == 2:
                        new.grid[i][j] = "S"
                        if error_check(new):
                            print("22_start")
                            undo(new,i,j)
                        else:
                            inrow["S"] = 1
                            inrow["M"] = 0
                        updated = True

                        # r_s_count +=1
                    elif inrow["S"] == 2:
                        new.grid[i][j] = "M"
                        if error_check(new):
                            undo(new,i,j)
                            print("23_start")
                        else:
                            inrow["M"] = 1
                            inrow["S"] = 0
                        updated = True
                        # r_m_count +=1
                    elif j<=3 and new.grid[i][j+1] == new.grid[i][j+2] and new.grid[i][j+1] != 'E':
                            if new.grid[i][j+1] == "M":
                                print("something")
                                new.grid[i][j] = "S"
                                if error_check(new):
                                    undo(new,i,j)
                                    print("32_norm")
                                else:
                                # r_s_count+=1
                                    inrow["S"]+=1
                                    inrow["M"] = 0
                            elif new.grid[i][j+1] == "S":
                                new.grid[i][j] = "M"
                                print("something")
                                if error_check(new):
                                    undo(new,i,j)
                                # r_m_count+=1
                                    print("33_norm")
                                else:
                                    inrow["M"]+=1
                                    inrow["S"] = 0
                    
                    elif inrow["M"] == 1 and j<=4 and new.grid[i][j+1] == "M":
                        new.grid[i][j] = "S"
                        updated = True
                        if error_check(new):
                            undo(new,i,j)
                            print("30_norm")
                        # r_s_count+=1
                        else:
                            inrow["S"] = 1
                            inrow["M"]= 0

                    elif inrow["S"] == 1 and s<=4 and new.grid[i][j+1] == "S":
                        new.grid[i][j] = "M"
                        updated = True
                        if error_check(new):
                            undo(new,i,j)
                            print("31_norm")
                        # r_m_count+=1
                        else:
                            inrow["M"] = 1
                            inrow["S"]= 0
                    if new.crosses[j+i*6]:
                        for num in new.crosses[j+i*6]:
                            if i == num//6 and new.grid[num//6][num%6] != "E":
                                if new.grid[num//6][num%6] == 'M':
                                    new.grid[i][j] = 'S'
                                elif new.grid[num//6][num%6] == 'S':
                                    new.grid[i][j] = 'M'
                                if error_check(new):
                                        print("24_cross")
                                        undo(new,i,j)
                                        undo(new,num//6,num%6)
                                else:
                                    if new.grid[num//6][num%6] == 'M':
                                        inrow["S"] += 1
                                        inrow["M"] = 0
                                    elif new.grid[num//6][num%6] == 'S':
                                        inrow["M"] += 1
                                        inrow["S"] = 0
                                 
                    if new.equals[j+i*6]:
                        for num in new.equals[j+i*6]: 
                            if i == num//6 and new.grid[num//6][num%6] == "E":
                                if r_m_count >= 2:
                                    new.grid[i][j] = "S"
                                    new.grid[num//6][num%6]="S"
                                    if error_check(new):
                                        print("25_eqal")
                                        undo(new,i,j)
                                        undo(new,num//6,num%6)
                                    else:
                                        inrow["S"]+=1
                                        inrow["M"]=0
                                    updated = True
                                    # r_s_count+=2
                                elif r_s_count >= 2:
                                    new.grid[i][j] = "M"
                                    new.grid[num//6][num%6]="M"
                                    if error_check(new):
                                        print("26_eqal")
                                        undo(new,i,j)
                                        undo(new,num//6,num%6)
                                    else:
                                        inrow["M"]+=1
                                        inrow["S"]=0
                                    updated = True
                                    # r_m_count+=2
                                elif inrow["M"]>=1:
                                    new.grid[i][j] = "S"
                                    new.grid[num//6][num%6]="S"
                                    if error_check(new):
                                        print("27_eqal")
                                        undo(new,i,j)
                                        undo(new,num//6,num%6)
                                    else:
                                        inrow["S"]+=1
                                        inrow["M"]=0
                                    updated = True
                                    # r_s_count+=2
                                elif inrow["S"]>=1:
                                    new.grid[i][j] = "M"
                                    new.grid[num//6][num%6]="M"
                                    if error_check(new):
                                        print("28_eqal")
                                        undo(new,i,j)
                                        undo(new,num//6,num%6)
                                    else:
                                        updated = True
                                        inrow["M"]+=1
                                        inrow["S"]=0
                                    # r_m_count+=2
                            elif i == num//6 and new.grid[num//6][num%6] != 'E':
                                    new.grid[i][j] = new.grid[num//6][num%6]
                                    if error_check(new):
                                        undo(new,i,j)
                                        print("29_eqal")
                                    else:
                                        if new.grid[num//6][num%6] == 'M':
                                            inrow['M']+=1
                                            inrow['S'] = 0
                                        else:
                                            inrow['S']+=1
                                            inrow['M'] = 0 
                    
                                
                    

        if not updated or error:
            # No changes made, terminate to prevent infinite loop
            print("No further changes can be made. Manual intervention or backtracking may be required.")
            break
    # print(new)
    return new 


tango = TangoBoard([["E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "S", "M"], ["E", "E", "E", "E", "M", "S"], ["M", "S", "E", "E", "E", "E"], ["S", "M", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E"]],[[], [2, 7], [1, 8], [], [], [], [], [1, 8], [2, 7], [], [], [], [], [], [], [21], [], [], [], [], [21], [15, 20], [], [], [], [], [], [], [], [], [], [], [], [], [], []],[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [15, 20], [14], [], [], [], [], [14], [], [], [], [], [], [], [28, 33], [27, 34], [], [], [], [], [27, 34], [28, 33], []])


# mang = TangoSolver(tango.grid,tango.crosses,tango.equals)
# mago = mang.get_solution()
mango = solved(tango)
print(tango)
print(mango)
