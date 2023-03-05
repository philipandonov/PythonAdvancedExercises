from collections import deque

materials = deque([int(x) for x in input().split()])
magic_level = deque([int(x) for x in input().split()])
gemstone = 0
porcelain = 0
gold = 0
diamond = 0
is_made = False
while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()
    sum_of_materials = current_material + current_magic
    if sum_of_materials < 100:
        if sum_of_materials % 2 == 0:
            current_material *= 2
            current_magic *= 3
            sum_of_materials = current_material + current_magic
        else:
            sum_of_materials *= 2

        if 100 <= sum_of_materials < 200:
            gemstone += 1
        elif 200 <= sum_of_materials < 300:
            porcelain += 1
        elif 300 <= sum_of_materials < 400:
            gold += 1
        elif 400 <= sum_of_materials < 500:
            diamond += 1
        else:
            continue
    elif sum_of_materials < 200:
        gemstone += 1
    elif sum_of_materials < 300:
        porcelain += 1
    elif sum_of_materials < 400:
        gold += 1
    elif sum_of_materials < 500:
        diamond += 1
    elif sum_of_materials >= 500:
        sum_of_materials /= 2
        if 100 <= sum_of_materials < 200:
            gemstone += 1
        elif 200 <= sum_of_materials < 300:
            porcelain += 1
        elif 300 <= sum_of_materials < 400:
            gold += 1
        elif 400 <= sum_of_materials < 500:
            diamond += 1
        else:
            continue
    if (gemstone > 0 and porcelain > 0) or (gold > 0 and diamond > 0):
        is_made = True
        break

if is_made:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(s) for s in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(s) for s in magic_level)}")
dict = {}
if gemstone > 0:
    dict['Gemstone:'] = gemstone
if porcelain > 0:
    dict['Porcelain Sculpture:'] = porcelain
if gold > 0:
    dict['Gold:'] = gold
if diamond > 0:
    dict['Diamond Jewellery:'] = diamond
for key, value in dict.items():
    if dict:
        print(f"{key} {value}")
