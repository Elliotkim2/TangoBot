import re
import sql
import datetime
import sys
import json

class TangoBoard:
    def __init__(self, grid, crosses, equals):
        self.grid = grid
        self.crosses = crosses
        self.equals = equals

    def __str__(self):
        return f"TangoBoard(grid={self.grid}, crosses={self.crosses}, equals={self.equals})"

    def to_dict(self):
        return {
            "grid": self.grid,
            "crosses": self.crosses,
            "equals": self.equals
        }
    def complete(self):
        for row in self.grid:
            if "E" in row:
                return False
        return True
    def get_column(self, col):
        columns = []
        for row in self.grid:
            columns.append(row[col])
        return columns
    def get_row_count(self, letter,row):
        count = 0
        for ele in self.grid[row]:
            if ele == letter:
                count+=1
        return count
    def get_col_count(self,letter,col):
        count = 0
        for row in self.grid:
            if row[col] == letter:
                count+=1
        return count 
    def update_grid(self,grid):
        self.grid = grid
    def print_board(self):
        return f"TangoBoard(grid={self.grid}"


def pairstolist(pairs):
    a = [[] for _ in range(36)]
    for i,j in pairs:
        a[i].append(j)
        a[j].append(i)
    return a

def filter(lines):
 
    # Get current date and time
    now_utc = datetime.datetime.utcnow()
    date = str(now_utc.date())

    count = 0

    inputs = []
    equals = []
    crosses = []

    additionals = []
    # this assumes the format of the page doesn't change
    for i,line in enumerate(lines):
        match = re.search(r'data-cell-idx', line)
        match1 = re.search(r'lotka-cell-edge lotka-cell-edge', line)
        if match:
            count+=1
            # print(i, match[0])
            inputs.append(lines[i+5])
            # print(i+5, lines[i+5])
            
        if match1:
            additionals.append((lines[i],lines[i+1],lines[i-10]))
    
    for i, line in enumerate(inputs):
        if "empty" in line:
            inputs[i] = "E"
        elif "Moon" in line: 
            inputs[i] = "M"
        elif "Sun" in line:
            inputs[i] = "S"

    for i, line in enumerate(additionals):
        if "Cross" in line[1]:
            match = re.search(r'data-cell-idx="(\d+)"', line[2])
            if match:
                cell_idx = int(match.group(1))
            if "right" in line[0]:
                crosses.append((cell_idx,cell_idx+1))
            elif "left" in line[0]:
                crosses.append((cell_idx,cell_idx-1))
            elif "down" in line[0]:
                crosses.append((cell_idx,cell_idx+6))
            else:
                crosses.append((cell_idx,cell_idx-6))
        if "Equal" in line[1]:
            match = re.search(r'data-cell-idx="(\d+)"', line[2])
            if match:
                cell_idx = int(match.group(1))
            if "right" in line[0]:
                equals.append((cell_idx,cell_idx+1))
            elif "left" in line[0]:
                equals.append((cell_idx,cell_idx-1))
            elif "down" in line[0]:
                equals.append((cell_idx,cell_idx+6))
            else:
                equals.append((cell_idx,cell_idx-6))
    # board = "".join(inputs)
    # grid = [[None]*6 for i in range(6)]
    # for i, _ in enumerate(board):
    #     grid[i//6][i%6] = board[i]

    crosses = pairstolist(crosses)
    equals = pairstolist(equals)
    currentBoard = TangoBoard(inputs, crosses, equals)

    json_data = json.dumps(currentBoard.to_dict())
    

    # print(board)
    if len(inputs) == 36:

        # sql.insert(date,json_data)
        print(date,json_data)
        with open("log.txt", "a") as file:
            file.write(date)
            file.write(json_data)
    else:
        raise Exception("Error in parsing Board.")