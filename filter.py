import re
import sql
import datetime

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

# this assumes the format of the page doesn't change
for i,line in enumerate(lines):
    match = re.search(r'data-cell-idx', line)
    if match:
        count+=1
        # print(i, match[0])
        inputs.append(lines[i+5])
        # print(i+5, lines[i+5])
for i, line in enumerate(inputs):
    if "empty" in line:
        inputs[i] = "E"
    elif "Moon" in line: 
        inputs[i] = "M"
    elif "Sun" in line:
        inputs[i] = "S"
board = "".join(inputs)
if len(board) == 36:
    sql.insert(date,board)
else:
    print("Something is off.")