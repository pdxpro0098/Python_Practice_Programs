sentence = "Write_a_Python_Program_to_convert_snake_case_to_camelCase"
def snakeToCamel(sentence):
    return sentence.replace("_", " ")

print(snakeToCamel(sentence))