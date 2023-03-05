row, col = [int(x) for x in input().split()]
matrix = []
max_sum_matrix = []
max_sum = -999999999999999999
for _ in range(row):
    matrix.append([int(x) for x in input().split()])
for r in range(row):
    for c in range(col):
        if r < row - 2 and c < col - 2:
            sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + \
                  matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2] \
                  + matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
            if max_sum < sum:
                max_sum = sum
                max_sum_matrix = [[matrix[r][c] for c in range(c, c+3)] for r in range(r, r+3)]

print(f"Sum = {max_sum}")
for i in range(3):
    print(" ".join(str(s) for s in max_sum_matrix[i]))

