n = int(input())
unique_elements = set()
for _ in range(n):
    elements = input().split()
    for el in elements:
        unique_elements.add(el)
print("\n".join(unique_elements))
