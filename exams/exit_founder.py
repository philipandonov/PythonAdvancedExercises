first_player, second_player = input().split(", ")
matrix = []
for row in range(6):
    matrix.append([x for x in input().split()])
turn = 0
first_player_hit_a_wall = False
second_player_hit_a_wall = False
while True:
    command = input().split(", ")
    current_row = int(command[0][1])
    current_col = int(command[1][0])
    turn += 1
    if turn % 2 == 1:
        current_player = first_player
    else:
        current_player = second_player
    if first_player_hit_a_wall and current_player == first_player:
        first_player_hit_a_wall = False
        continue
    if second_player_hit_a_wall and current_player == second_player:
        second_player_hit_a_wall = False
        continue

    if matrix[current_row][current_col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    if matrix[current_row][current_col] == "T":
        if current_player == first_player:
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        else:
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
    if matrix[current_row][current_col] == "W":
        if current_player == first_player:
            first_player_hit_a_wall = True
            print(f"{current_player} hits a wall and needs to rest.")

        else:
            second_player_hit_a_wall = True
            print(f"{current_player} hits a wall and needs to rest.")

