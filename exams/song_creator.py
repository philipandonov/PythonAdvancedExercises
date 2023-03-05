def add_songs(*args):
    dictionary = {}
    song_name = ''

    for key, value in args:
        if key not in dictionary:
            dictionary[key] = value
        else:
            dictionary[key] += value
    for key, value in dictionary.items():
        song_name += f"- {key}\n"
        song_name += '\n'.join(x for x in value)
        if value:
            song_name += '\n'

    return song_name


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))

