number_rows = int(input())
matrix = []
for _ in range(number_rows):
    matrix.append([int(x) for x in input().split()])
while True:
    command = input()
    if command == 'END':
        break
    current_command = command.split()
    row = int(current_command[1])
    col = int(current_command[2])
    value = int(current_command[3])
    if not 0 <= row < number_rows or not 0 <= col < number_rows:
        print("Invalid coordinates")
        continue
    if current_command[0] == "Add":
        matrix[row][col] += value

    elif current_command[0] == "Subtract":
        matrix[row][col] -= value
for row in matrix:
    print(*row, sep=" ")