from collections import deque

string = deque(input().split())
main_colours = []
secondary_colours = []
while string:
    if len(string) == 1:
        first_substring = string.pop()
        last_substring = first_substring
        concatenate_string = last_substring
    else:

        first_substring = string.popleft()
        last_substring = string.pop()
        concatenate_string = first_substring + last_substring
    if concatenate_string == "red":
        main_colours.append("red")
    elif concatenate_string == "yellow":
        main_colours.append("yellow")
    elif concatenate_string == "blue":
        main_colours.append("blue")
    else:
        if first_substring == last_substring:
            if first_substring[:-1] != "":
                string.insert((len(string) - 1) // 2, first_substring[:-1])

        else:
            if first_substring[:-1] != "":
                string.insert((len(string) - 1) // 2, first_substring[:-1])
            if last_substring[:-1] != "":
                string.insert((len(string) - 1) // 2, last_substring[:-1])
print(main_colours)
print(string)
