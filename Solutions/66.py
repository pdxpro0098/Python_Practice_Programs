def removeDuplicateValues(dictionary):
    result = {}
    seen_values = set()
    for key, value in dictionary.items():
        if value not in seen_values:
            result[key] = value
            seen_values.add(value)
    return result


dict1 = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 4,
    "F": 4,
}


d = removeDuplicateValues(dict1)
print(d)