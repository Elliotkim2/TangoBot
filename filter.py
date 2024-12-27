import re
import sql
import datetime
# class TangoL:
#     def __init__(self,x,y,string):
#         self.x = x
#         self.y = y
#         self.string = string
#         self.cross = None
#         self.equal = None
#     def update_cross(self, cross):
#         self.cross = cross
#     def updata_equal(self,equal):
#         self.equal = equal
    
        
# Get current date and time
now = datetime.datetime.now()
date = str(now.date())

with open("html.txt", "r") as f:
    lines = f.readlines()

# Create an empty array
array = []

# Iterate over each line in the file
for line in lines:
    # Append the line to the array
    array.append(line.strip())  # .strip() removes trailing newlines
count = 0

inputs = []
equals=[]
crosses=[]

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
        if "left" in line[0]:
            crosses.append((cell_idx,cell_idx-1))
        if "down" in line[0]:
            crosses.append((cell_idx,cell_idx+6))
        else:
            crosses.append((cell_idx,cell_idx-6))
    if "Equal" in line[1]:
        match = re.search(r'data-cell-idx="(\d+)"', line[2])
        if match:
            cell_idx = int(match.group(1))
        if "right" in line[0]:
            equals.append((cell_idx,cell_idx+1))
        if "left" in line[0]:
            equals.append((cell_idx,cell_idx-1))
        if "down" in line[0]:
            equals.append((cell_idx,cell_idx+6))
        else:
            equals.append((cell_idx,cell_idx-6))
        
print(crosses)
print(equals)

board = "".join(inputs)
if len(board) == 36:
    sql.insert(date,board)
else:
    print("Something is off.")