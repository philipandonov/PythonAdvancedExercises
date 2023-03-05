number_1, number_2 = input().split()
first_collection = set()
second_collection = set()
third_collection = set()
for _ in range(int(number_1)):
    number = int(input())
    first_collection.add(number)
for _ in range(int(number_2)):
    number = int(input())
    second_collection.add(number)
third_collection = first_collection & second_collection
print("\n".join(str(x) for x in third_collection))