number_rows = int(input())
matrix = []

for _ in range(number_rows):
    matrix.append([x for x in input().split()])


def index_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def up_direction(rol, coll, matx):
    current_sum = 0
    current_direction = []
    while True:
        rol -= 1
        if index_valid(rol, coll, number_rows):
            if matx[rol][coll] == "X":
                break
            else:
                current_sum += int(matx[rol][coll])
                current_direction.append([rol, coll])
        else:
            break
    return current_sum, current_direction


def down_direction(rol, coll, matx):
    current_sum = 0
    current_direction = []
    while True:
        rol += 1
        if index_valid(rol, coll, number_rows):
            if matx[rol][coll] == "X":
                break
            else:
                current_sum += int(matx[rol][coll])
                current_direction.append([rol, coll])
        else:
            break
    return current_sum, current_direction


def left_direction(rol, coll, matx):
    current_sum = 0
    current_direction = []
    while True:
        coll -= 1
        if index_valid(rol, coll, number_rows):
            if matx[rol][coll] == "X":
                break
            else:
                current_sum += int(matx[rol][coll])
                current_direction.append([rol, coll])
        else:
            break
    return current_sum,current_direction


def right_direction(rol, coll, matx):
    current_sum = 0
    current_direction = []
    while True:
        coll += 1
        if index_valid(rol, coll, number_rows):
            if matx[rol][coll] == "X":
                break
            else:
                current_sum += int(matx[rol][coll])
                current_direction.append([rol, coll])
        else:
            break
    return current_sum, current_direction


best_sum = float('-inf')
best_direction = []
direction = ''
for row in range(number_rows):
    for col in range(number_rows):
        if matrix[row][col] == "B":
            up_sum, up_dir = up_direction(row, col, matrix)
            down_sum, down_dir = down_direction(row, col, matrix)
            left_sum, left_dir = left_direction(row, col, matrix)
            right_sum, right_dir = right_direction(row, col, matrix)
            if up_sum > best_sum and up_dir:
                best_sum = up_sum
                best_direction = up_dir
                direction = 'up'
            if down_sum > best_sum and down_dir:
                best_sum = down_sum
                best_direction = down_dir
                direction = 'down'
            if left_sum > best_sum and left_dir:
                best_sum = left_sum
                best_direction = left_dir
                direction = 'left'
            if right_sum > best_sum and right_dir:
                best_sum = right_sum
                best_direction = right_dir
                direction = 'right'

print(direction)
for direct in best_direction:

    print(direct)
print(best_sum)