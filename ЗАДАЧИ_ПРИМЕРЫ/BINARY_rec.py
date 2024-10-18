
"""Поиск элемента в списке, рекурсией """

def binary_search(lst, search_item, left_position, right_position):
    if right_position < left_position:
        return None

    middle_elem = (left_position + right_position) // 2
    if lst[middle_elem] == search_item:
        return middle_elem
    if lst[middle_elem] > search_item:
        return binary_search(lst, search_item, left_position, middle_elem - 1)
    else:
        return binary_search(lst, search_item, middle_elem + 1, right_position)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_item = 4

index_item = binary_search(lst, search_item, left_position=0, right_position=(len(lst) - 1))
print(index_item)
