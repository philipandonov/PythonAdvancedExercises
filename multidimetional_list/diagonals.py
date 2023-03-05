size_of_matrix = int(input())
matrix = []
sum_first = 0
sum_second = 0
primary_diagonal = []
secondary_diagonal = []
for i in range(size_of_matrix):
    matrix.append([int(x) for x in input().split(", ")])
    sum_first += matrix[i][i]
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][(size_of_matrix - 1) - i])
    sum_second += matrix[i][(size_of_matrix - 1) - i]


print(f"Primary diagonal: {', '.join(str(s) for s in primary_diagonal)}. Sum: {sum_first}")
print(f"Secondary diagonal: {', '.join(str(s) for s in secondary_diagonal)}. Sum: {sum_second}")
