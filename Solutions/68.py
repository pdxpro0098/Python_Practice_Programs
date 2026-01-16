# Krish's Approach
dictionary = {'b': 4, 'a': 2, 'd': 1, 'c': 3}


def sortDictByValue(d):
    return dict(sorted(d.items(), key=lambda item: item[0]))


sorted_dict = sortDictByValue(dictionary)
print(sorted_dict)

# Dalip's Approach
my_dict = {3:"dalipkumar",5:"krish",2:"tripti",1:"elon"}

res = dict(sorted(my_dict.items()))
print(res)
