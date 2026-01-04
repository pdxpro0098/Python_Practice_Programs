
pwd = "Krish@1234"

symbol = ["!", "@", "#", "$", "%", "^", "&", "*",
          "(", ")", "_", "+", "-", "=", "{", "}",
          "[", "]", "|", ":", ";", "< ", ">", ".",
          "?", "/", "~"]

def checkPwd(pwd):
    if len(pwd) < 8:
        print("short length")
        return False
    if pwd.isalpha():
        print("must  contain num")
        return False
    if not any(char in symbol for char in pwd):
        print("must  contain symbol")
        return False
    return True


print(checkPwd(pwd))
