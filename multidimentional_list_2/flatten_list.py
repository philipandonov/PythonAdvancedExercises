flatten_list = input().split("|")
matrix = []

for part_list in flatten_list:
    current_list = part_list.split()
    list_to_append = []
    for num in current_list:
        if num != " ":
            list_to_append.append(num)

    matrix.append(list_to_append)
matrix.reverse()
for row in matrix:
    if row:
        print(*row, sep= ' ', end= " ")
