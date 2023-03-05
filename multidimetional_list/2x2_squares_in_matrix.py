row, col = [int(x) for x in input().split()]
matrix = []
number_of_squares = 0
for _ in range(row):
    matrix.append([s for s in input().split()])
for r in range(row):
    for c in range(col):
        if r < row-1 and c < col-1:
            if matrix[r][c] == matrix[r+1][c]\
                    and matrix[r+1][c] == matrix[r+1][c+1]\
                    and matrix[r+1][c+1] == matrix[r][c+1]:
                number_of_squares += 1


print(number_of_squares)
