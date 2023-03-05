n = int(input())
matrix = []
sum_first = 0
sum_second = 0
for i in range(n):
    matrix.append([int(x) for x in(input().split())])
    sum_first += matrix[i][i]
    sum_second += matrix[i][(n-1) - i]
diff = abs(sum_first - sum_second)
print(diff)