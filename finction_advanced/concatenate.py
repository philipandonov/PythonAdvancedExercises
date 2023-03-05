def concatenate(*args, **kwargs):
    final_string = ''
    for word in args:
        final_string += word
    for key, value in kwargs.items():
        if key in final_string:
            final_string = final_string.replace(key, value)

    return final_string


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
