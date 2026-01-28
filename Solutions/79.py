# Krish's Approach

pwd = "Krish@1234"

symbol = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "+",
    "-",
    "=",
    "{",
    "}",
    "[",
    "]",
    "|",
    ":",
    ";",
    "< ",
    ">",
    ".",
    "?",
    "/",
    "~",
]


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


# Dalip's Approach
print("Password Rules:-")
print("Password should have at-least 8 digits.")
print("Password should have at-least 1 upper letter.")
print("Password should have at-least 1 special letter.")
print("Password should have at-least one number.")

attempt = 3

has_digit = False
has_special = False
one_capital = False
while attempt > 0:
    password = input("Enter password: ")
    if len(password) >= 8:
        for ch in password:
            ascii_val = ord(ch)

            if 48 <= ascii_val and ascii_val <= 57:  # 48-57
                has_digit = True

            if (
                32 >= ascii_val <= 47
                or 58 >= ascii_val <= 64
                or 91 >= ascii_val <= 96
                or 123 >= ascii_val <= 126
            ):
                has_special = True

            if 65 <= ascii_val <= 90:
                one_capital = True

        if has_digit and has_special and one_capital:
            print("Access Granted✅")
            break
        else:
            attempt -= 1
            print(f"❌ Invalid Password. Attempt left: {attempt}")
    else:
        attempt -= 1
        print(f"❌ Password too short. Attempt left: {attempt}")

if attempt == 0:
    print("🔒 Account Locked")
