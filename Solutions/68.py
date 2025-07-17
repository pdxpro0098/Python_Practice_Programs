dictionary = {'b': 4, 'a': 2, 'd': 1, 'c': 3}


def sortDictByValue(d):
    return dict(sorted(d.items(), key=lambda item: item[0]))


sorted_dict = sortDictByValue(dictionary)
print(sorted_dict)
