from enum import unique

text = input()
unique_symbols = {}

for chr in text:
    if chr not in unique_symbols:
        unique_symbols[chr] = 1
    else:
        unique_symbols[chr] += 1
sorted_unique_symbols = sorted(unique_symbols.items(), key=lambda x: x[0])

for key, value in sorted_unique_symbols:
    print(f"{key}: {value} time/s")