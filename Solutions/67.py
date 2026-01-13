# krish's approach
dict1 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

dict2 = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
}

dict1.update(dict2)
print(dict1)

# Dalip's Approach
my_dict = {"food":"cuisine","week":"fragile"}
my_dict1 = {"slow":"sluggish"}


merged_dict = {**my_dict,**my_dict1}
print(merged_dict)
