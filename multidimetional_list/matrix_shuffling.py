row, col = [int(x) for x in input().split()]
matrix = []
for _ in range(row):
    matrix.append([s for s in input().split()])
while True:
    command = input()
    if command == "END":
        break
    current_command = command.split()
    if current_command[0] != "swap" \
            or len(current_command) != 5 \
            or not 0 <= int(current_command[1]) < row \
            or not 0 <= int(current_command[2]) < col \
            or not 0 <= int(current_command[3]) < row \
            or not 0 <= int(current_command[4]) < col:
        print("Invalid input!")
        continue
    else:
        row_1 = int(current_command[1])
        col_1 = int(current_command[2])
        row_2 = int(current_command[3])
        col_2 = int(current_command[4])

        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]

    for i in range(len(matrix)):
        print(" ".join(matrix[i]))
