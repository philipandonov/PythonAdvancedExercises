n = int(input())
even = set()
odd = set()
for i in range(1, n+1):
    name = [ord(x) for x in input()]
    value_of_the_name = int(sum(name)/i)
    if value_of_the_name % 2 == 0:
        even.add(value_of_the_name)
    else:
        odd.add(value_of_the_name)
if sum(even) == sum(odd):
    union = even.union(odd)
    print(", ".join(str(x) for x in union))
elif sum(even) < sum(odd):
    difference = odd.difference(even)
    print(", ".join(str(x) for x in difference))
else:
    symetric = even.symmetric_difference(odd)
    print(", ".join(str(x) for x in symetric))
