def words_sorting(*args):
    dicti = {}
    for key in args:
        value = 0
        for v in key:
            value += ord(v)
        dicti[key] = value
    sum_of_values = sum(dicti.values())
    if sum_of_values % 2 == 1:
        sorted_dict = sorted(dicti.items(), key=lambda x: -x[1])
    else:
        sorted_dict = sorted(dicti.items(), key=lambda x: x[0])
    result = ''
    for key, value in sorted_dict:
        result += key + " - " + str(value) + "\n"

    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
