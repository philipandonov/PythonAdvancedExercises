from collections import deque


number_of_stations = int(input())
a_map = deque()
for _ in range(number_of_stations):
    a_map.append([int(x) for x in input().split()])

for index in range(number_of_stations):
    tank = 0
    failed = False
    for fuel, distance in a_map:
        tank += fuel
        if tank < distance:
            failed = True
            break
        else:

            tank -= distance
    if failed:
        a_map.append(a_map.popleft())
    else:
        print(index)
        break