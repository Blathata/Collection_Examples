def merge(left: list[int], right: list[int]) -> list[int]:
    """Сортирует и обьединяет 2 списка.

    Args:
        left (list[int]): Список для сортировки
        right (list[int]): Список для сортировки

    Returns:
        list[int]: Отсортированый список.
    """
    result: list = []
    left_idx: int = 0
    right_idx: int = 0  
    len_left: int = len(left)
    len_right: int = len(right)
    
    while left_idx < len_left and right_idx < len_right:
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    return result + left[left_idx:] + right[right_idx:] 

lst_1 = [2, 4, 6, 8]
lst_2 = [1, 3, 5, 7]

print(merge(lst_1, lst_2))