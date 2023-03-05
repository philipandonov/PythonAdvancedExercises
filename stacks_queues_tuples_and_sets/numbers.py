first_sequence = set(int(el) for el in input().split())
second_sequence = set(int(el) for el in input().split())
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'Add':
        if command[1] == 'First':
            current_sequence = {int(x) for x in command[2:]}
            first_sequence = first_sequence.union(current_sequence)
        elif command[1] == 'Second':
            current_sequence = {int(x) for x in command[2:]}
            second_sequence = second_sequence.union(current_sequence)

    elif command[0] == 'Remove':
        if command[1] == 'First':
            current_sequence = {int(x) for x in command[2:]}
            first_sequence = first_sequence.difference(current_sequence)
        elif command[1] == 'Second':
            current_sequence = {int(x) for x in command[2:]}
            second_sequence = second_sequence.difference(current_sequence)
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
