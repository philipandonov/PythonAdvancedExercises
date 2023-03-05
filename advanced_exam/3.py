def forecast(*args):
    weather = {"Sunny": [], "Cloudy": [], "Rainy": []}
    print(args)
    for value, key in args:
        weather[key].append(value)
    str_to_print = ''
    for key, value in weather.items():
        if value:
            sorted_value = sorted(value)
            for val in sorted_value:
                str_to_print += val + " - " + key + "\n"

    return str_to_print


print(forecast(
    ["Tokyo", "Rainy"],
    ("Sofia", "Rainy")))


