numbers_of_names = int(input())
names = set()
for _ in range(numbers_of_names):
    username = input()
    names.add(username)
print('\n'.join(names))
