from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
flowers = {
    1: "rose",
    2: "tulip",
    3: "lotus",
    4: "daffodil"
}
flowers_manipulating = {
    1: "rose",
    2: "tulip",
    3: "lotus",
    4: "daffodil"
}
found_a_word = False
while consonants and vowels:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for key, value in flowers_manipulating.items():
        if current_vowel in value:
            current_value = value.replace(current_vowel, "")
            value = current_value
            flowers_manipulating[key] = current_value
        if current_consonant in value:
            cur_val = value.replace(current_consonant, "")
            value = cur_val
            flowers_manipulating[key] = cur_val
        if value == "":
            found_a_word = True
            print(f"Word found: {flowers[key]}")
            break

    if found_a_word:
        break
if not found_a_word:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")