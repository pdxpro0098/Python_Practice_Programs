numStr1 = "12345"
numStr2 = "123K45"


def onlyString(string):
    try:
        string = int(string)
        return True
    except:
        return False


print(onlyString(numStr2))