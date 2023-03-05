from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
signs = deque(input().split())
total_honey = 0
while bees and nectar:
    first_bee = bees.popleft()
    last_nectar = nectar.pop()
    if first_bee <= last_nectar:
        current_sign = signs.popleft()
        if current_sign == '+':
            total_honey += first_bee + last_nectar
        elif current_sign == '-':
            total_honey += abs(first_bee - last_nectar)
        elif current_sign == '*':
            total_honey += first_bee * last_nectar
        elif current_sign == '/':
            if first_bee and last_nectar > 0:
                total_honey += first_bee / last_nectar
            else:
                continue

    else:
        bees.appendleft(first_bee)
print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")