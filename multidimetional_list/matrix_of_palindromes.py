row, col = input().split()
matrix = []

for r in range(int(row)):
    matrix.append([])
    for c in range(int(col)):

        matrix[r].append(f'{chr(97 + r)}' + f'{chr(97 + c + r)}' + f'{chr(97 + r)}')
for i in range(len(matrix)):
    print(" ".join(matrix[i]))
