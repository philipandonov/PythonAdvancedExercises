row, col = [int(x) for x in input().split()]
matrix = []
word = input()
word_index = 0
for row_index in range(row):
    matrix.append([0 for el in range(col)])

for row_index in range(row):
    for col_index in range(col):
        matrix[row_index][col_index] = word[word_index]
        word_index += 1
        if word_index == len(word):
            word_index = 0
for row_index in range(row):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    print("".join(matrix[row_index]))