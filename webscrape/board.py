import re
import datetime
import sys
import json

class TangoBoard:
    def __init__(self, grid, crosses, equals, date=None):
        self.grid = grid
        self.crosses = crosses
        self.equals = equals
        self.date = date

    def __str__(self):
        return f"TangoBoard(grid={self.grid}, crosses={self.crosses}, equals={self.equals}, date={self.date})"

    def to_dict(self):
        return {
            "grid": self.grid,
            "crosses": self.crosses,
            "equals": self.equals,
            "date": self.date
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


def filter(lines):
    # Get current date and time
    now_utc = datetime.datetime.utcnow()
    date = str(now_utc.date())

    count = 0

    cells = []
    equals = []
    crosses = []

    additionals = []
    entry = []
    new_lines = []
    copy = False
    for line in lines:
        if '<section class="lotka-board' in line:
            copy = True
        if '</section>' in line:
            copy = False
        if copy:
            new_lines.append(line)
    lines = new_lines


    for i,line in enumerate(lines):
        if 'data-cell-idx' in line:
            # cells.append([lines[i+5]])
            if "empty" in lines[i+5]:
                cells.append(["E"])
            elif "Moon" in lines[i+5]: 
                cells.append(["M"])
            elif "Sun" in lines[i+5]:
                cells.append(["S"])
        if 'lotka-cell-edge--right' in line:
            if 'Equal' in lines[i+1]:
                cells[-1].append(("Equal","right"))
            else:
                cells[-1].append(("Cross","right"))
        if 'lotka-cell-edge--down' in line:
            if 'Equal' in lines[i+1]:
                cells[-1].append(("Equal","down"))
            else:
                cells[-1].append(("Cross","down"))
    # this assumes the format of the page doesn't change  

    grid = []
    crosses = [[] for _ in range(36)]
    equals = [[] for _ in range(36)]
    for i, cell in enumerate(cells):
        grid.append(cell[0])
        for edge in cell[1:]:
            t = i+1 if edge[1] == 'right' else i+6
            if edge[0] == 'Cross':
                crosses[i].append(t)
                crosses[t].append(i)
            else:
                equals[i].append(t)
                equals[t].append(i)
    currentBoard = TangoBoard(grid, crosses, equals, date)
    return currentBoard