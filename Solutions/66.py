# Krish's Approach
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


# Dalip's Approach
def removeDuplicateValuesFromDictionary(apartement):
    unique = {}
    for key,value in apartment.items():
        if value not in unique.values():
            unique[key] = value
    return unique

apartment = {
    1:"1st Floor",
    2:"2nd Floor",
    3:"3rd Floor",
    4:"1st Floor",
    5:"5th Floor"
}
    
print(f"After removing duplicates values: {removeDuplicateValuesFromDictionary(apartment)}")
