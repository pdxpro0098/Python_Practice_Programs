def is_pangram(s):
    alphabets = "abcdefghijklmnopqrstuvwxyz "

    for char in range(len(s)):
        if s[char].lower() not in alphabets:
            return False
    return True


print(is_pangram("The quick brown fox jumps over the lazy dog"))
