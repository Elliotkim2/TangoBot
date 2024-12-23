import re
with open("html.txt", "r") as f:
    lines = f.readlines()

# Create an empty array
array = []

# Iterate over each line in the file
for line in lines:
    # Append the line to the array
    array.append(line.strip())  # .strip() removes trailing newlines
count = 0
# for i,line in enumerate(lines):
#     match = re.search(r'xmlns="http://www.w3.org/2000/svg" aria-label="(Empty|Moon|Sun)"', line)
#     if match:
#         count+=1
#         print(i, match[0])
inputs = []
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
print(inputs)
grid = [[None]*6 for i in range(6)]
for i, _ in enumerate(inputs):
    grid[i//6][i%6] = inputs[i]
for line in grid:
    print(line)
# print(count)
# print(array)