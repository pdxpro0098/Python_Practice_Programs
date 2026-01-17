# Krish's Approach
dictionary = {'a': 4, 'b': 2, 'c': 1, 'd': 3}


def sortDictByValue(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))


sorted_dict = sortDictByValue(dictionary)
print(sorted_dict)

# Dalip's Approach
my_dict = {"dalipkumar":3,"krish":5,"jeff":2,"elon":1}

res =dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(res)
