n = int(input())
ss = []
for _ in range(n):
    comm = input().split()
    command = comm[0]
    if command == '1':
        number = int(comm[1])
        ss.append(number)

    elif command == '2' and ss:
        ss.pop()
    elif command == '3' and ss:
        print(max(ss))
    elif command == '4' and ss:
        print(min(ss))
while ss:
    element = ss.pop()
    if ss:
        print(element, end=', ')
    else:
        print(element)