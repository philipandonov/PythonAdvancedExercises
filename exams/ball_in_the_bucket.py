matrix = []
for row in range(6):
    matrix.append(input().split())

points = 0
for turn in range(3):
    command = input().split(", ")
    current_row = int(command[0][1::])
    current_col = int(command[1][:-1])
    if 0 <= current_row <= 5 and 0 <= current_col <= 5:
        if matrix[current_row][current_col] == "B":
            matrix[current_row][current_col] = "-"
            for row in range(6):
                if row != current_row:
                    points += int(matrix[row][current_col])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif points >= 300:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
