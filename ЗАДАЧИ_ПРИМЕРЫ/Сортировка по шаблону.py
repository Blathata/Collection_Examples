def sort_box(recived_boxs: list[int], pattern: list[int]) -> list[int]:
    """
    Принемает на вход массив для сортировки и массив-шаблон, 
    в соответствии с которым должна быть выполнена сортировка.

    Args:
        recived_boxs (list[int]): Числа которые надо отсортировать
        pattern (list[int]): Шаблон, для сортировки.

    Returns:
        list[int]: _description_
    """
    res = []
    counter_pattern: int = 0
    
    while len(pattern) > counter_pattern:
        for i in range(len(recived_boxs)):
            if pattern[counter_pattern] == recived_boxs[i]:
                res.append(recived_boxs[i])
            else:
                continue
        counter_pattern += 1

    return res + sorted(list(int(i) for i in recived_boxs if i not in pattern))
                
    
recived_boxs = [2, 2, 4, 3, 5, 6, 0, 9, 8, 7, 7]
pattern = [2, 4, 3, 5, 6, 0,]

print(sort_box(recived_boxs, pattern)) # [2, 2, 4, 3, 5, 6, 0, 7, 7, 8, 9]
