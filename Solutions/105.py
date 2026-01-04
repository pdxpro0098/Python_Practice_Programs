mixedLst = [1, "str", [1, 2, 3], "str", 1, [1, 2, 3], 2.2, "str", 1, 2.2, 2.2]

def move_to_end(lst, dtype):
    front = [x for x in lst if not isinstance(x, dtype)]
    back = [x for x in lst if isinstance(x, dtype)]
    return front + back

res = move_to_end(mixedLst, str)
print("Move lists to end:", res)