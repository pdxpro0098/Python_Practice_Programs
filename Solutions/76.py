# Krish's Approach
s = "remove duplicate duplicate words from from this string string"
noDuplicate = set(s.split(" "))

print(sorted(noDuplicate))


# Dalip's Approach
def sortInAlphanumericOrder(w):
    n = len(w)
    for i in range(n):
        for j in range(n - 1):
            if w[j] > w[j + 1]:
                w[j], w[j + 1] = w[j + 1], w[j]
    return ",".join(w)


input_str = "dalip,krish,dalip,elon,43"
words = input_str.split(",")
result = []

[result.append(x) for x in words if x not in result]
# print(result)
print(f"{sortInAlphanumericOrder(result)}")
