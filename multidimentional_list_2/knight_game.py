def index_check(rol, co, size):
    if 0 <= rol < size and 0 <= co < size:
        return True
    return False


def knight_moves(roll, coll, mtr):
    current_attacked_knights = 0
    if index_check(roll - 2, coll - 1, number_rows):
        if mtr[roll - 2][coll - 1] == "K":
            current_attacked_knights += 1
    if index_check(roll - 2, coll + 1, number_rows):
        if mtr[roll - 2][coll + 1] == "K":
            current_attacked_knights += 1
    if index_check(roll - 1, coll - 2, number_rows):
        if mtr[roll - 1][coll - 2] == "K":
            current_attacked_knights += 1
    if index_check(roll - 1, coll + 2, number_rows):
        if mtr[roll - 1][coll + 2] == "K":
            current_attacked_knights += 1
    if index_check(roll + 1, coll + 2, number_rows):
        if mtr[roll + 1][coll + 2] == "K":
            current_attacked_knights += 1
    if index_check(roll + 1, coll - 2, number_rows):
        if mtr[roll + 1][coll - 2] == "K":
            current_attacked_knights += 1
    if index_check(roll + 2, coll - 1, number_rows):
        if mtr[roll + 2][coll - 1] == "K":
            current_attacked_knights += 1
    if index_check(roll + 2, coll + 1, number_rows):
        if mtr[roll + 2][coll + 1] == "K":
            current_attacked_knights += 1
    return current_attacked_knights


number_rows = int(input())
matrix = []
knights = 0
for row in range(number_rows):
    matrix.append([x for x in input()])
    for col in range(number_rows):
        if matrix[row][col] == "K":
            knights += 1
removed_knights = 0
while True:
    if knights == 0:
        break
    attacked_knights = 0
    current_position = ()

    for row in range(number_rows):
        for col in range(number_rows):
            if matrix[row][col] == "K":
                current_knights = knight_moves(row, col, matrix)
                if current_knights > attacked_knights:
                    attacked_knights = current_knights
                    current_position = (row, col)
    if attacked_knights > 0:
        matrix[current_position[0]][current_position[1]] = "0"
        removed_knights += 1
        knights -= 1
    else:
        break
print(removed_knights)
