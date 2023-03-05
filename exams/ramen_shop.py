from collections import deque

bows_of_ramen = deque([int(x) for x in input().split(', ')])
customer = deque([int(x) for x in input().split(', ')])

while True:

    if not customer:
        print("Great job! You served all the customers.")
        if bows_of_ramen:
            print(f"Bowls of ramen left: {', '.join(str(s) for s in bows_of_ramen)}")
        break
    if not bows_of_ramen:
        print("Out of ramen! You didn't manage to serve all customers.")
        if customer:
            print(f"Customers left: {', '.join(str(s)for s in customer)}")
        break
    current_bow = bows_of_ramen.pop()
    current_customer = customer.popleft()
    if current_customer == current_bow:
        continue
    if current_bow > current_customer:
        current_bow -= current_customer
        bows_of_ramen.append(current_bow)
        continue
    if current_customer > current_bow:
        current_customer -= current_bow
        customer.appendleft(current_customer)
        continue


