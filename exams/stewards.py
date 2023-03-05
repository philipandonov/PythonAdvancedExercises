from collections import deque

plane_seats = [x for x in input().split(", ")]
first_numbers = deque([int(x) for x in input().split(", ")])
second_numbers = deque([int(x) for x in input().split(", ")])
taken_seats = []
rotation = 0
while True:
    first_number = first_numbers.popleft()
    last_number = second_numbers.pop()
    rotation += 1
    character = chr(first_number + last_number)
    passenger_number_1 = str(first_number) + character
    passenger_number_2 = str(last_number) + character
    if passenger_number_1 in plane_seats:
        plane_seats.remove(passenger_number_1)
        taken_seats.append(passenger_number_1)
    elif passenger_number_2 in plane_seats:
        plane_seats.remove(passenger_number_2)
        taken_seats.append(passenger_number_2)
    elif passenger_number_1 in taken_seats or passenger_number_2 in taken_seats:
        continue
    else:
        first_numbers.append(first_number)
        second_numbers.appendleft(last_number)
    if rotation == 10:
        break

    if len(taken_seats) == 3:
        break

print(f'Seat matches: {", ".join(x for x in taken_seats)}')
print(f'Rotations count: {rotation}')
