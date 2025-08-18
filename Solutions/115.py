lst = [1, 2, 3, 4, 5]


def next_number_after_pop(lst):
    if len(lst) > 1:
        lst.pop(0)
        return lst[0]
    else:
        return None


print(next_number_after_pop(lst))