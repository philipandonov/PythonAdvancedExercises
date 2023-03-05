from collections import deque

milligrams_of_caffeine = deque([int(x) for x in input().split(', ')])
energy_drinks = deque([int(x) for x in input().split(', ')])
total_caffeine = 0
while milligrams_of_caffeine and energy_drinks:
    current_milligrams = milligrams_of_caffeine.pop()
    current_energy = energy_drinks.popleft()
    current_caffeine_in_drink = current_milligrams * current_energy
    if total_caffeine + current_caffeine_in_drink <= 300:
        total_caffeine += current_caffeine_in_drink
    else:
        energy_drinks.append(current_energy)
        if total_caffeine - 30 > 0:
            total_caffeine -= 30
if energy_drinks:
    print(f"Drinks left: {', '.join(str(s) for s in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")