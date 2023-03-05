def up_side(rol):
    current_alice_row = rol - 1
    return current_alice_row


def down_side(rol):
    current_alice_row = rol + 1
    return current_alice_row


def left_side(coll):
    current_alice_col = coll - 1
    return current_alice_col


def right_side(coll):
    current_alice_col = coll + 1
    return current_alice_col


size_of_matrix = int(input())
matrix = []

for _ in range(size_of_matrix):
    matrix.append([x for x in input().split()])
alice_row = 0
alice_col = 0
for row in range(size_of_matrix):
    for col in range(size_of_matrix):
        if matrix[row][col] == "A":
            alice_row = row
            alice_col = col
tea_collected = 0

while True:
    if tea_collected >= 10:
        matrix[alice_row][alice_col] = "*"
        break
    command = input()
    if command == "up":
        matrix[alice_row][alice_col] = "*"
        alice_row = up_side(alice_row)
        if alice_row < 0 or alice_col < 0 or alice_row >= size_of_matrix or alice_col >= size_of_matrix:
            print("Alice didn't make it to the tea party.")
            break
        elif matrix[alice_row][alice_col] == "R":
            matrix[alice_row][alice_col] = "*"
            print("Alice didn't make it to the tea party.")
            break
        else:
            if matrix[alice_row][alice_col] != "." and matrix[alice_row][alice_col] != "*":
                tea_collected += int(matrix[alice_row][alice_col])
            matrix[alice_row][alice_col] = 'A'
    if command == "down":
        matrix[alice_row][alice_col] = "*"
        alice_row = down_side(alice_row)
        if alice_row < 0 or alice_col < 0 or alice_row >= size_of_matrix or alice_col >= size_of_matrix:
            print("Alice didn't make it to the tea party.")
            break
        elif matrix[alice_row][alice_col] == "R":
            matrix[alice_row][alice_col] = "*"
            print("Alice didn't make it to the tea party.")
            break
        else:
            if matrix[alice_row][alice_col] != "." and matrix[alice_row][alice_col] != "*":
                tea_collected += int(matrix[alice_row][alice_col])
            matrix[alice_row][alice_col] = 'A'
    if command == "left":
        matrix[alice_row][alice_col] = "*"
        alice_col = left_side(alice_col)
        if alice_row < 0 or alice_col < 0 or alice_row >= size_of_matrix or alice_col >= size_of_matrix:
            print("Alice didn't make it to the tea party.")
            break
        elif matrix[alice_row][alice_col] == "R":
            matrix[alice_row][alice_col] = "*"
            print("Alice didn't make it to the tea party.")
            break
        else:
            if matrix[alice_row][alice_col] != "." and matrix[alice_row][alice_col] != "*":
                tea_collected += int(matrix[alice_row][alice_col])
            matrix[alice_row][alice_col] = 'A'
    if command == "right":
        matrix[alice_row][alice_col] = "*"
        alice_col = right_side(alice_col)

        if alice_row < 0 or alice_col < 0 or alice_row >= size_of_matrix or alice_col >= size_of_matrix:
            print("Alice didn't make it to the tea party.")
            break
        elif matrix[alice_row][alice_col] == "R":
            matrix[alice_row][alice_col] = "*"
            print("Alice didn't make it to the tea party.")
            break
        else:
            if matrix[alice_row][alice_col] != "." and matrix[alice_row][alice_col] != "*":
                tea_collected += int(matrix[alice_row][alice_col])
            matrix[alice_row][alice_col] = 'A'
if tea_collected >= 10:
    print("She did it! She went to the party.")
for row in matrix:
    print(*row, sep=" ")
