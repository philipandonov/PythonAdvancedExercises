def even_odd_filter(**kwargs):
    dictionary = {}
    for key, value in kwargs.items():
        if key == "odd":
            result = [x for x in value if x % 2 == 1]
            dictionary[key] = result
        elif key == "even":
            result = [x for x in value if x % 2 == 0]
            dictionary[key] = result
    sorted_dict = sorted(dictionary.items(), key=lambda x: -len(x[1]))
    final_dict = {}
    for key,value in sorted_dict:
        final_dict[key] = value
    return final_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
