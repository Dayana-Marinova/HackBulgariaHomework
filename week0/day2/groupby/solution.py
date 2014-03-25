def groupby(func, seq):
    dictionary = {}
    for i in seq:
        dictionary[func(i)] = []
    for i in seq:
        for key in dictionary:
            if key == func(i):
                dictionary[key].append(i)
    return dictionary
