# Krish's Approach
sentence = "Write_a_Python_Program_to_convert_snake_case_to_camelCase"


def snakeToCamel(sentence):
    return sentence.replace("_", " ")


print(snakeToCamel(sentence))


# Dalip's Approach
import re


def snakeToCamel(t):
    camel = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)
    return camels


text = "dalip_kumar"
print(f"Snake Case : {text}\nCamel Case: {snakeToCamel(text)}")
