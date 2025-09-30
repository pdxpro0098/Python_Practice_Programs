# Dalip's Approach
import re


def validateInequality(expr):
    expr = expr.replace(" ", "")

    if not re.search(r"(<=|>=|!=|>|<)", expr):
        return False

    pattern = r"^[a-zA-Z0-9+-/%*]+(<=|>=|!=|<|>)[a-zA-Z0-9+-/%*]+$"
    return bool(re.match(pattern, expr))


print(validateInequality("3+1 == 5"))  # false
print(validateInequality("y/2 >= 4"))  # True
