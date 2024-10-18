def break_into_blocks(array: list[int]):
    """ Получает на вход массив и возвращает максимальное число блоков, 
    на которое можно разбить этот массив

    Args:
        array (list[int]): Список

    Returns:
        _type_: Возвращает максимальное число блоков
    """

    blocks = 0
    max_so_far = 0
    for i, ai in enumerate(array):
        max_so_far = max(max_so_far, ai)
        if max_so_far == i:
            blocks += 1
    return blocks

n = [3, 2, 0, 1, 4, 6, 5]     
print(break_into_blocks(n))