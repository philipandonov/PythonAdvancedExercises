import collections
from collections import deque

chocolate = deque([int(x) for x in input().split(', ')])
milk_cups = deque([int(x) for x in input().split(', ')])
milkshakes = 0
has_milkshakes = False
while milk_cups and chocolate:

    last_chocolate = chocolate.pop()
    first_milk_cup = milk_cups.popleft()
    if last_chocolate <= 0 and first_milk_cup <= 0:
        continue
    if first_milk_cup <= 0 and last_chocolate > 0:
        chocolate.append(last_chocolate)
        continue
    if last_chocolate <= 0 and first_milk_cup > 0:
        milk_cups.appendleft(first_milk_cup)
        continue

    if last_chocolate == first_milk_cup:
        milkshakes += 1
    else:
        milk_cups.append(first_milk_cup)
        chocolate.append(last_chocolate - 5)
    if milkshakes == 5:
        has_milkshakes = True
        break
if has_milkshakes:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print('Chocolate: empty')
if milk_cups:
    print(f"Milk: {', '.join(str(milk) for milk in milk_cups)}")
else:
    print("Milk: empty")