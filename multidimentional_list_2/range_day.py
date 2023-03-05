def validate_position(row, col):
    if 0 <= row < 5 and 0 <= col < 5:
        return False
    return True


matrix = []
for _ in range(5):
    matrix.append([x for x in input().split()])
number_of_commands = int(input())
targets = 0
for row in range(5):
    for col in range(5):
        if matrix[row][col] == 'A':
            current_row = row
            current_col = col
        if matrix[row][col] == 'x':
            targets += 1
hit_targets = []
for _ in range(number_of_commands):
    command = input().split()
    if command[0] == 'move':
        step = int(command[2])
        if command[1] == 'down':
            if validate_position(current_row + step, current_col):
                continue
            if not matrix[current_row + step][current_col] == '.':
                continue
            matrix[current_row][current_col] = '.'
            current_row += step
            matrix[current_row][current_col] = 'A'

        elif command[1] == 'up':
            if validate_position((current_row - step), current_col):
                continue
            if not matrix[current_row - step][current_col] == '.':
                continue
            matrix[current_row][current_col] = '.'
            current_row -= step
            matrix[current_row][current_col] = 'A'
        elif command[1] == 'right':
            if validate_position(current_row, current_col + step):
                continue
            if not matrix[current_row][current_col + step] == '.':
                continue
            matrix[current_row][current_col] = '.'
            current_col += step
            matrix[current_row][current_col] = 'A'
        elif command[1] == 'left':
            if validate_position(current_row, current_col - step):
                continue
            if not matrix[current_row][current_col - step] == '.':
                continue
            matrix[current_row][current_col] = '.'
            current_col -= step
            matrix[current_row][current_col] = 'A'

    elif command[0] == 'shoot':
        current_rol = current_row
        current_coll = current_col
        if command[1] == 'down':
            while True:
                current_rol += 1
                if validate_position(current_rol, current_coll):
                    break
                if matrix[current_rol][current_coll] == 'x':
                    matrix[current_rol][current_coll] = '.'
                    hit_targets.append((current_rol, current_coll))
                    break

        elif command[1] == 'up':
            while True:
                current_rol -= 1
                if validate_position(current_rol, current_coll):
                    break
                if matrix[current_rol][current_coll] == 'x':
                    matrix[current_rol][current_coll] = '.'
                    hit_targets.append([current_rol, current_coll])
                    break

        elif command[1] == 'right':
            while True:
                current_coll += 1
                if validate_position(current_rol, current_coll):
                    break
                if matrix[current_rol][current_coll] == 'x':
                    matrix[current_rol][current_coll] = '.'
                    hit_targets.append((current_rol, current_coll))
                    break
        elif command[1] == 'left':
            while True:
                current_coll -= 1
                if validate_position(current_rol, current_coll):
                    break
                if matrix[current_rol][current_coll] == 'x':
                    matrix[current_rol][current_coll] = '.'
                    hit_targets.append((current_rol, current_coll))
                    break
if targets == len(hit_targets):
    print(f"Training completed! All {targets} targets hit.")

else:
    print(f"Training not completed! {targets - len(hit_targets)} targets left.")
for target in hit_targets:
    print(f'[{target[0]}, {target[1]}]')
