lst = [2, 4, 7, 9]
n = 5


def find_position(element, lst):
    i = 0
    inserted = False
    for item in lst:
        if element == item:
            break
        elif element < item:
            inserted = True
            break
        i = i + 1
    if not inserted:
        return len(lst)
    else:
        return i


r = find_position(n, lst)
print(r)
