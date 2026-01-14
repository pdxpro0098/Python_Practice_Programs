# Krish's Approach
string1 = " Write a Python Program to check if a string contains any special character."
special_characters = ["!", "@", "#", "$", "%", "&", "^", "*",
                      "(", ")", "\"", "\\", "/", "?", ".", ",",
                      "'", "+", "-", "=", "_", ":", ";", "<",
                      ">", "]", "[", "}", "{", "|",]


def isContainSpecialCharacter(string):
    for char in string:
        if char in special_characters:
            return 1
    return 0

print(isContainSpecialCharacter(string1))


# Dalip's Approach
# The special characters
# !  @  #  $  %  ^  &  *  (  )
# -  _  =  +  [  ]  {  }  |
# \  :  ;  "  '  <  >  ,  .  ?
# /  ~  `  space

specialChars = [ 
    "!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , 
    "(" , ")" ,"-" , "_" , "=" , "+" , "[" , "]" , 
    "{" , "}" ,"|" ,"\\" , ":" , ";" , "\"" , "'" , 
    "<" , ">" , "," , "." , "?" ,"/" , "~" , "`" , " " ]

name= "dalip_kumar"
for sp in specialChars:
    if sp in name:
        print(sp)
