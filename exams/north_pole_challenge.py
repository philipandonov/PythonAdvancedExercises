size_of_matrix = input().split(',')
rows = int(size_of_matrix[0])
cols = int(size_of_matrix[1])
decorations = 0
gifts = 0
cookies = 0
item_counter = 0
matrix = []
for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == "Y":
            current_row = row
            current_col = col
        elif matrix[row][col] != ".":
            item_counter += 1

while True:
    command = input()
    if command == "End":
        break

    comm = command.split("-")
    direction = comm[0]
    steps = int(comm[1])
    for _ in range(steps):
        if direction == 'up':
            matrix[current_row][current_col] = "x"
            current_row -= 1
            if current_row == -1:
                current_row = rows - 1
            if matrix[current_row][current_col] == "D":
                decorations += 1
                item_counter -= 1
            elif matrix[current_row][current_col] == "G":
                gifts += 1
                item_counter -= 1
            elif matrix[current_row][current_col] == "C":
                cookies += 1
                item_counter -= 1
            matrix[current_row][current_col] = "Y"

        elif direction == 'down':
            matrix[current_row][current_col] = "x"
            current_row += 1
            if current_row == rows:
                current_row = 0
            if matrix[current_row][current_col] == "D":
                decorations += 1
                item_counter -= 1
            elif matrix[current_row][current_col] == "G":
                gifts += 1
                item_counter -= 1
            elif matrix[current_row][current_col] == "C":
                cookies += 1
                item_counter -= 1
            matrix[current_row][current_col] = "Y"
        elif direction == 'left':
            matrix[current_row][current_col] = "x"
            current_col -= 1
            if current_col == -1:
                current_col = cols- 1
            if matrix[current_row][current_col] == "D":
                decorations += 1
                item_counter -= 1
            elif matrix[current_row][current_col] == "G":
                gifts += 1
                item_counter -= 1
            elif matrix[current_row][current_col] == "C":
                cookies += 1
                item_counter -= 1
            matrix[current_row][current_col] = "Y"
        elif direction == "right":
            matrix[current_row][current_col] = "x"
            current_col += 1
            if current_col == cols:
                current_col = 0
            if matrix[current_row][current_col] == "D":
                decorations += 1
                item_counter -= 1
            elif matrix[current_row][current_col] == "G":
                gifts += 1
                item_counter -= 1
            elif matrix[current_row][current_col] == "C":
                cookies += 1
                item_counter -= 1
            matrix[current_row][current_col] = "Y"
        if item_counter == 0:
            break
    if item_counter == 0:
        print("Merry Christmas!")
        break
print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
for r in matrix:
    print(*r, sep=' ')