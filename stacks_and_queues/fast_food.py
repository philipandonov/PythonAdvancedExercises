from collections import deque


quantity = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))
having_food = True
while orders:

    if quantity >= orders[0]:
        quantity -= orders[0]
        orders.popleft()
    else:
        having_food = False
        break

if having_food:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")




