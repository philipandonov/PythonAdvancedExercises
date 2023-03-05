def start_spring(**kwargs):
    dictionary = {}
    for value, key in kwargs.items():
        if key not in dictionary:
            dictionary[key] = [value]
        else:
            dictionary[key].append(value)
    sorted_dict = sorted(dictionary.items(), key=lambda x: (-len(x[0]), x[0]))
    str_to_print = ''
    for key, value in sorted_dict:
        sorted_value = sorted(value)
        str_to_print += key + ":" + "\n"
        for val in sorted_value:
            str_to_print += "-" + val + "\n"
    return str_to_print


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }

print(start_spring(**example_objects))
