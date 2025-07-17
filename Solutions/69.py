dictionary = {'a': 4, 'b': 2, 'c': 1, 'd': 3}


def sortDictByValue(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))


sorted_dict = sortDictByValue(dictionary)
print(sorted_dict)
