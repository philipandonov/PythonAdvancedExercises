clothes = [int(x) for x in input().split()]
capacity = int(input())
counter = 1
current_capacity = capacity
while clothes:

    if clothes[-1] <= current_capacity:
        current_capacity -= clothes[-1]
        clothes.pop()
    else:
        counter += 1
        current_capacity = capacity
print(counter)
