lst = [2, 3, 5, 6, 8]
n = 7


def find_position(element, lst):
    
    pos_idx = 0
    for i in lst:
        if n > i:
            pos_idx += 1
        elif n < i:
            break
        elif n == i:
            break
        else:
            pos_idx = len(lst)
    return pos_idx
        


r = find_position(n, lst)
print(r)