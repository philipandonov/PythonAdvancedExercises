parentheses = input()
is_balanced = True
opening_brackets = []
mirror_brackets = {'(': ')', '{': '}', '[': ']',}
for p in parentheses:
    if p in "([{":
        opening_brackets.append(p)
    else:
        if opening_brackets:
            if not mirror_brackets[opening_brackets.pop()] == p:
                is_balanced = False
                break
        else:
            is_balanced = False
            break
if is_balanced:
    print("YES")
else:
    print("NO")


