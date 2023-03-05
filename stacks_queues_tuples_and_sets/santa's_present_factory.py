from collections import deque

materials = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])
presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
crafted_presents = []
while magic and materials:
    last_material = materials.pop()
    first_magic = magic.popleft()
    total_magic = last_material * first_magic
    if total_magic in presents:
        crafted_presents.append(presents[total_magic])
    else:
        if total_magic < 0:
            sum_of_magic = first_magic + last_material
            materials.append(sum_of_magic)
        elif total_magic > 0:
            materials.append(last_material + 15)
        else:
            if first_magic == 0:
                materials.append(last_material)
                continue
            if last_material == 0:
                magic.appendleft(first_magic)
                continue
            if first_magic == 0 and last_material == 0:
                continue
if ('Wooden train' in crafted_presents and 'Doll' in crafted_presents) \
        or ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print('No presents this Christmas!')
if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

if crafted_presents:
    sorted_presents = set(crafted_presents)
    for present in sorted(sorted_presents):
        print(f"{present}: {crafted_presents.count(present)}")
