numbers_to_letters = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h'
}
numbers_to_numbers = {
    0: '8',
    1: '7',
    2: '6',
    3: '5',
    4: '4',
    5: '3',
    6: '2',
    7: '1'
}
matrix = []
for row in range(8):
    matrix.append([x for x in input().split()])
    for col in range(8):
        if matrix[row][col] == "w":
            white_row = row
            white_col = col
        elif matrix[row][col] == "b":
            black_row = row
            black_col = col

turns = 1
while True:

    if turns % 2 == 1:
        if 0 < white_col < 7:
            if matrix[white_row - 1][white_col - 1] == "b":
                white_row -= 1
                white_col -= 1
                print(
                    f"Game over! White win, capture on {numbers_to_letters[white_col]}{numbers_to_numbers[white_row]}.")
                break
            elif matrix[white_row - 1][white_col + 1] == "b":
                white_row -= 1
                white_col += 1
                print(
                    f"Game over! White win, capture on {numbers_to_letters[white_col]}{numbers_to_numbers[white_row]}.")
                break
            else:
                matrix[white_row][white_col] = '-'
                white_row -= 1
                matrix[white_row][white_col] = "w"

        elif white_col == 0:
            if matrix[white_row - 1][white_col + 1] == "b":
                white_row -= 1
                white_col += 1
                print(
                    f"Game over! White win, capture on {numbers_to_letters[white_col]}{numbers_to_numbers[white_row]}.")
                break
            else:
                matrix[white_row][white_col] = '-'
                white_row -= 1
                matrix[white_row][white_col] = "w"
        elif white_col == 7:
            if matrix[white_row - 1][white_col - 1] == "b":
                white_row -= 1
                white_col -= 1
                print(
                    f"Game over! White win, capture on {numbers_to_letters[white_col]}{numbers_to_numbers[white_row]}.")
                break
            else:
                matrix[white_row][white_col] = '-'
                white_row -= 1
                matrix[white_row][white_col] = "w"
        if white_row == 0:
            print(
                f"Game over! White pawn is promoted to a queen at {numbers_to_letters[white_col]}{numbers_to_numbers[white_row]}.")
            break

    else:
        if 0 < black_col < 7:
            if matrix[black_row + 1][black_col - 1] == "w":
                black_row += 1
                black_col -= 1
                print(
                    f"Game over! Black win, capture on {numbers_to_letters[black_col]}{numbers_to_numbers[black_row]}.")
                break

            elif matrix[black_row + 1][black_col + 1] == "w":
                black_row += 1
                black_col += 1
                print(
                    f"Game over! Black win, capture on {numbers_to_letters[black_col]}{numbers_to_numbers[black_row]}.")
                break
            else:
                matrix[black_row][black_col] = '-'
                black_row += 1
                matrix[black_row][black_col] = "b"
        if black_col == 0:
            if matrix[black_row + 1][black_col + 1] == "w":
                black_row += 1
                black_col += 1
                print(
                    f"Game over! Black win, capture on {numbers_to_letters[black_col]}{numbers_to_numbers[black_row]}.")
                break
            else:
                matrix[black_row][black_col] = '-'
                black_row += 1
                matrix[black_row][black_col] = "b"
        if black_col == 7:
            if matrix[black_row + 1][black_col - 1] == "w":
                black_row += 1
                black_col -= 1
                print(
                    f"Game over! Black win, capture on {numbers_to_letters[black_col]}{numbers_to_numbers[black_row]}.")
                break
            else:
                matrix[black_row][black_col] = '-'
                black_row += 1
                matrix[black_row][black_col] = "b"
        if black_row == 7:
            print(
                f"Game over! Black pawn is promoted to a queen at {numbers_to_letters[black_col]}{numbers_to_numbers[black_row]}.")
            break
    turns += 1
