def naughty_or_nice_list(*args, **kwargs):
    list_of_kids = args[0]
    dict_of_kids = {"Nice": [], "Naughty": [], 'Not found': []}
    for comm in args[1::]:
        (num), behav = comm.split("-")
        counter = 0
        current_kid = ""
        current_tuple = tuple()
        for n in list_of_kids:
            if int(num) == n[0]:
                counter += 1
                current_kid = n[1]
                current_tuple = n
        if counter == 1:
            dict_of_kids[behav].append(current_kid)
            list_of_kids.remove(current_tuple)

    for key, value in kwargs.items():
        count = 0
        cur_tup = tuple()
        for child in list_of_kids:
            if key == child[1]:
                count += 1
                cur_tup = child
        if count == 1:
            dict_of_kids[value].append(key)
            list_of_kids.remove(cur_tup)
    for child in list_of_kids:
        dict_of_kids['Not found'].append(child[1])
    str_to_print = ''
    for key,value in dict_of_kids.items():
        if dict_of_kids[key]:
            str_to_print += key + ": " + ", ".join(value) + "\n"
    return str_to_print


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
