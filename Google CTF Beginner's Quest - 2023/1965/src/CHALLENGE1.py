# Predefined strings from the DATA statements
DATA = [
    ["M","R","_","_","T","_","M","S","N","_","R"],
    ["A","I","I","A","W","D","E","I","A","A","A"],
    ["T","X","S","_","O","I","N","O","L","R","Y"]
]

# Read by column and flatten the matrix
flag = []
num_rows = len(DATA)
num_cols = len(DATA[0])

for col in range(num_cols):
    for row in range(num_rows):
        flag.append(DATA[row][col])

flag = ''.join(flag)

# Print the flag
print("FLAG{"+flag+"}")