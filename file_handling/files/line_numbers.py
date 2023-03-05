from string import punctuation


with open("files/text.txt", "r") as file_to_read:
    text = file_to_read.readlines()

with open("files/result.txt", "a") as result_file:
    lines = 0
    for line in text:
        lines += 1
        char = 0
        symbol = 0
        for character in line:
            if character.isalpha():
                char += 1
            elif character in punctuation:
                symbol += 1

        result_file.write(f"Line {lines}: {line[:-1]} ({char})({symbol})" + "\n")

