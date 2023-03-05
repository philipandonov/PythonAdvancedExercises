
matrix = []
for _ in range(6):
    matrix.append([x for x in input().split()])
my_position = input().split(', ')
current_row = int(my_position[0][1])
current_col = int(my_position[1][0])
current_position = matrix[current_row][current_col]
command = input()
while command != "Stop":
    current_command = command.split(', ')
    curr_command = current_command[0]
    direction = current_command[1]
    if direction == "up":
        current_row = current_row - 1
    elif direction == "down":
        current_row = current_row + 1
    elif direction == "left":
        current_col = current_col - 1
    elif direction == "right":
        current_col = current_col + 1
    if curr_command == "Create":
        if matrix[current_row][current_col] == ".":
            matrix[current_row][current_col] = current_command[2]
        else:
            command = input()
            continue
    elif curr_command == "Update":
        if matrix[current_row][current_col] != ".":
            matrix[current_row][current_col] = current_command[2]
        else:
            command = input()
            continue
    elif curr_command == "Delete":
        if matrix[current_row][current_col] != ".":
            matrix[current_row][current_col] = '.'
        else:
            command = input()
            continue
    elif curr_command == "Read":
        if matrix[current_row][current_col] != ".":
            print(matrix[current_row][current_col])
        else:
            command = input()
            continue

    command = input()
for cow in matrix:
    print(*cow, sep=" ")
