lst = [0, 5, 4, 3, 2, 3]


def valid_mountain_array(lst):
    lift = 0
    descent = 0
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            if descent:  # если не None
                return False
            lift += 1
        elif lst[i] > lst[i+1]:
            if not lift:  # если None
                return False
            descent += 1
        else:
            return False
    return bool(lift and descent)


print(valid_mountain_array(lst))
