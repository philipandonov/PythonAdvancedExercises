from collections import deque

matrix = []
for row in range(6):
    matrix.append([x for x in input().split()])
    for col in range(6):
        if matrix[row][col] == "E":
            current_row = row
            current_col = col
movements = deque(input().split(", "))
deposits = {"W": "Water deposit", "M": "Metal deposit", "C": "Concrete deposit"}
found_deposits = []
has_deposit = False
while movements:
    current_move = movements.popleft()
    if current_move == "down":
        current_row += 1
        if current_row == 6:
            current_row = 0
    elif current_move == "up":
        current_row -= 1
        if current_row == -1:
            current_row = 5
    elif current_move == "left":
        current_col -= 1
        if current_col == -1:
            current_col = 5
    elif current_move == "right":
        current_col += 1
        if current_col == 6:
            current_col = 0
    if matrix[current_row][current_col] in deposits.keys():
        found_deposits.append(matrix[current_row][current_col])
        print(
            f"{deposits[matrix[current_row][current_col]]} found at ({current_row}, {current_col})")
        current_row + 1
        if current_row == 6:
            current_row = 0
        current_col + 1
        if current_col == 6:
            current_col = 0
    if "W" in found_deposits and "M" in found_deposits and "C" in found_deposits:
        has_deposit = True
    if matrix[current_row][current_col] == "R":
        print(f"Rover got broken at ({current_row}, {current_col})")
        break

if has_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")