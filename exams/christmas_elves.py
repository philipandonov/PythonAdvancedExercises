from collections import deque

elf_energy = deque([int(x) for x in input().split()])
box_materials = deque([int(x) for x in input().split()])

total_energy = 0
total_made_toys = 0
turn_counter = 0
while elf_energy and box_materials:
    current_elf_energy = elf_energy.popleft()
    current_box_material = box_materials.pop()

    if current_elf_energy < 5:
        box_materials.append(current_box_material)
        continue
    turn_counter += 1

    if turn_counter % 3 == 0:
        if current_elf_energy >= 2 * current_box_material:
            total_made_toys += 2
            total_energy += 2 * current_box_material
            current_elf_energy -= 2 * current_box_material
            current_elf_energy += 1
            if turn_counter % 5 == 0:
                total_made_toys -= 2
                current_elf_energy -= 1
                elf_energy.append(current_elf_energy)
            continue
        else:
            current_elf_energy *= 2
            elf_energy.append(current_elf_energy)
            box_materials.append(current_box_material)
            continue

    elif current_elf_energy >= current_box_material:
        total_made_toys += 1
        total_energy += current_box_material
        current_elf_energy -= current_box_material
        current_elf_energy += 1
        if turn_counter % 5 == 0:
            total_made_toys -= 1
            current_elf_energy -= 1
        elf_energy.append(current_elf_energy)
    else:
        current_elf_energy *= 2
        elf_energy.append(current_elf_energy)
        box_materials.append(current_box_material)


print(f"Toys: {total_made_toys}")
print(f"Energy: {total_energy}")
if elf_energy:
    print(f"Elves left: {', '.join(str(s) for s in elf_energy)}")

if box_materials:
    print(f"Boxes left: {', '.join(str(s) for s in box_materials)}")
