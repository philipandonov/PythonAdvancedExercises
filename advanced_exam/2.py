size_of_matrix = int(input())
racing_number = input()
matrix = []
for row in range(size_of_matrix):
    matrix.append(input().split())
current_row = 0
current_col = 0
matrix[current_row][current_col] = "C"
total_km = 0
while True:
    command = input()

    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break
    elif command == "left":
        matrix[current_row][current_col] = "."
        current_col -= 1
    elif command == "right":
        matrix[current_row][current_col] = "."
        current_col += 1
    elif command == "up":
        matrix[current_row][current_col] = "."
        current_row -= 1
    elif command == "down":
        matrix[current_row][current_col] = "."
        current_row += 1
    if matrix[current_row][current_col] == ".":
        total_km += 10
    elif matrix[current_row][current_col] == "T":
        matrix[current_row][current_col] = "."
        for row in range(size_of_matrix):
            for col in range(size_of_matrix):
                if matrix[row][col] == "T":
                    current_row = row
                    current_col = col
                    matrix[current_row][current_col] = "."
        total_km += 30
    elif matrix[current_row][current_col] == "F":
        total_km += 10
        print(f"Racing car {racing_number} finished the stage!")
        break
print(f"Distance covered {total_km} km.")
matrix[current_row][current_col] = "C"
for row in range(size_of_matrix):
    print(*matrix[row], sep="")
