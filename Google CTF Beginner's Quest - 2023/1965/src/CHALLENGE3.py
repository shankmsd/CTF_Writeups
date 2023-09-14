# Define the constants
PREFIX = 5
FL = 60
SL = 12

# Predefined values from the DATA statements
S = [72, 69, 76, 76, 79, 71, 89, 78, 86, 65, 69, 76]
F = [
    24, 0, 30, 10, 10, 4, 13, 17, 5, 4, 6, 30,
    13, 6, 21, 19, 24, 14, 13, 6, 9, 4, 29, 15,
    4, 16, 31, 5, 25, 2, 6, 10, 31, 18, 15, 25,
    6, 6, 24, 5, 0, 9, 6, 15, 24, 5, 26, 3,
    6, 0, 19, 24, 6, 10, 28, 17, 6, 0, 1, 109
]

# Initialize the string
U = [""] * (PREFIX + FL + 1)

# Reverse XOR encryption
for i in range(1, int(FL / SL) + 1):
    for j in range(1, SL + 1):
        k = SL * (i - 1) + j
        U[k + PREFIX] = chr(S[j - 1] ^ F[k - 1])
flag = "".join(U)

# Print the flag
print("FLAG{"+flag+"}")