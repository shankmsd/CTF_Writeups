W = 5
H = 7
O = [
    31, 1, 1, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 31, 14, 17, 17, 31, 17, 17, 17, 14, 1, 1, 25, 17, 17, 14, 12, 2, 2, 1,
    2, 2, 12, 0, 17, 17, 17, 30, 16, 14, 14, 17, 25, 21, 19, 17, 14, 0, 0, 17, 17, 17, 17, 14, 0, 0, 0, 0, 0, 0,
    31, 4, 4, 14, 4, 4, 4, 24, 15, 16, 16, 15, 16, 16, 15, 15, 16, 16, 15, 16, 16, 15, 0, 0, 0, 0, 0, 0, 31, 31,
    1, 1, 15, 1, 1, 1, 0, 0, 0, 0, 0, 0, 31, 15, 16, 16, 15, 16, 16, 15, 4, 6, 4, 4, 4, 4, 4, 14, 1, 1, 25, 17,
    17, 14, 1, 1, 15, 17, 17, 17, 17, 31, 16, 16, 8, 8, 4, 4, 0, 0, 0, 0, 0, 0, 31, 31, 1, 1, 31, 1, 1, 31, 17,
    17, 17, 10, 10, 4, 4, 31, 1, 1, 31, 1, 1, 31, 15, 17, 17, 15, 17, 17, 17, 17, 17, 10, 4, 4, 4, 4, 17, 17,
    21, 21, 21, 27, 17, 17, 17, 17, 31, 17, 17, 17, 15, 16, 16, 15, 16, 16, 15, 0, 0, 30, 1, 1, 1, 1, 15, 16,
    16, 15, 16, 16, 15, 3, 4, 4, 8, 4, 4, 3
]

with open("C1_Flag.txt", "w", encoding='utf-8') as file:
    for i in range(0, len(O), H):
        for ii in range(H):
            for iii in range(W):
                file.write("■" if (O[i + ii] >> iii) & 1 else " ")
            file.write("\n")
        file.write("\n")