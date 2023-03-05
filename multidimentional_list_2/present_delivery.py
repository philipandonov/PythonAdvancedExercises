def validate_position(row, col):
    if 0 <= row < 5 and 0 <= col < 5:
        return False
    return True


presents_of_santa = int(input())
size_of_matrix = int(input())
matrix = []
for _ in range(size_of_matrix):
    matrix.append([x for x in input().split()])
naughty_kids = 0
nice_kids = 0
happy_kids = 0
have_nice_kids = False
for row in range(size_of_matrix):
    for col in range(size_of_matrix):
        if matrix[row][col] == "S":
            santa_row = row
            santa_col = col
        if matrix[row][col] == "X":
            naughty_kids += 1
        if matrix[row][col] == "V":
            nice_kids += 1
            have_nice_kids = True
while True:

    command = input()
    if command == "Christmas morning":
        break
    if presents_of_santa == 0:
        print("Santa ran out of presents!")
        break
    if command == "down":
        if validate_position(santa_row + 1, santa_col):
            continue
        matrix[santa_row][santa_col] = '-'
        santa_row += 1
        if matrix[santa_row][santa_col] == 'X':
            naughty_kids -= 1
            matrix[santa_row][santa_col] = 'S'
        elif matrix[santa_row][santa_col] == 'V':
            nice_kids -= 1
            happy_kids += 1
            presents_of_santa -= 1
            matrix[santa_row][santa_col] = 'S'

        elif matrix[santa_row][santa_col] == "C":
            matrix[santa_row][santa_col] = 'S'
            if matrix[santa_row + 1][santa_col] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row + 1][santa_col] = '-'
            elif matrix[santa_row + 1][santa_col] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row + 1][santa_col] = '-'
            if matrix[santa_row - 1][santa_col] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row - 1][santa_col] = '-'
            elif matrix[santa_row - 1][santa_col] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row - 1][santa_col] = '-'
            if matrix[santa_row][santa_col + 1] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col + 1] = '-'
            elif matrix[santa_row][santa_col + 1] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col + 1] = '-'
            if matrix[santa_row][santa_col - 1] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col - 1] = '-'
            elif matrix[santa_row][santa_col - 1] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col - 1] = '-'
        else:
            matrix[santa_row][santa_col] = 'S'
    elif command == 'up':
        if validate_position(santa_row - 1, santa_col):
            continue
        matrix[santa_row][santa_col] = '-'
        santa_row -= 1
        if matrix[santa_row][santa_col] == 'X':
            naughty_kids -= 1
            matrix[santa_row][santa_col] = 'S'
        elif matrix[santa_row][santa_col] == 'V':
            nice_kids -= 1
            happy_kids += 1
            presents_of_santa -= 1
            matrix[santa_row][santa_col] = 'S'

        elif matrix[santa_row][santa_col] == "C":
            matrix[santa_row][santa_col] = 'S'
            if matrix[santa_row + 1][santa_col] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row+1][santa_col] = '-'
            elif matrix[santa_row + 1][santa_col] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row + 1][santa_col] = '-'
            if matrix[santa_row - 1][santa_col] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row - 1][santa_col] = '-'
            elif matrix[santa_row - 1][santa_col] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row - 1][santa_col] = '-'
            if matrix[santa_row][santa_col + 1] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col+1] = '-'
            elif matrix[santa_row][santa_col + 1] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col + 1] = '-'
            if matrix[santa_row][santa_col - 1] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col - 1] = '-'
            elif matrix[santa_row][santa_col - 1] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col - 1] = '-'
        else:
            matrix[santa_row][santa_col] = 'S'
    elif command == 'left':
        if validate_position(santa_row, santa_col - 1):
            continue
        matrix[santa_row][santa_col] = '-'
        santa_col -= 1
        if matrix[santa_row][santa_col] == 'X':
            naughty_kids -= 1
            matrix[santa_row][santa_col] = 'S'
        elif matrix[santa_row][santa_col] == 'V':
            nice_kids -= 1
            happy_kids += 1
            presents_of_santa -= 1
            matrix[santa_row][santa_col] = 'S'

        elif matrix[santa_row][santa_col] == "C":
            matrix[santa_row][santa_col] = 'S'
            if matrix[santa_row + 1][santa_col] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row + 1][santa_col] = '-'
            elif matrix[santa_row + 1][santa_col] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row + 1][santa_col] = '-'
            if matrix[santa_row - 1][santa_col] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row - 1][santa_col] = '-'
            elif matrix[santa_row - 1][santa_col] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row - 1][santa_col] = '-'
            if matrix[santa_row][santa_col + 1] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col + 1] = '-'
            elif matrix[santa_row][santa_col + 1] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col + 1] = '-'
            if matrix[santa_row][santa_col - 1] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col - 1] = '-'
            elif matrix[santa_row][santa_col - 1] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col - 1] = '-'
        else:
            matrix[santa_row][santa_col] = 'S'
    elif command == 'right':
        if validate_position(santa_row, santa_col + 1):
            continue
        matrix[santa_row][santa_col] = '-'
        santa_col += 1
        if matrix[santa_row][santa_col] == 'X':
            naughty_kids -= 1
            matrix[santa_row][santa_col] = 'S'
        elif matrix[santa_row][santa_col] == 'V':
            nice_kids -= 1
            happy_kids += 1
            presents_of_santa -= 1
            matrix[santa_row][santa_col] = 'S'

        elif matrix[santa_row][santa_col] == "C":
            matrix[santa_row][santa_col] = 'S'
            if matrix[santa_row + 1][santa_col] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row + 1][santa_col] = '-'
            elif matrix[santa_row + 1][santa_col] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row + 1][santa_col] = '-'
            if matrix[santa_row - 1][santa_col] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row - 1][santa_col] = '-'
            elif matrix[santa_row - 1][santa_col] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row - 1][santa_col] = '-'
            if matrix[santa_row][santa_col + 1] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col + 1] = '-'
            elif matrix[santa_row][santa_col + 1] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col + 1] = '-'
            if matrix[santa_row][santa_col - 1] == 'X':
                naughty_kids -= 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col - 1] = '-'
            elif matrix[santa_row][santa_col - 1] == 'V':
                nice_kids -= 1
                happy_kids += 1
                presents_of_santa -= 1
                matrix[santa_row][santa_col - 1] = '-'
        else:
            matrix[santa_row][santa_col] = 'S'
    if presents_of_santa == 0:
        print("Santa ran out of presents!")
        break

for row in matrix:
    print(*row, sep=' ')
if nice_kids == 0 and have_nice_kids:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
