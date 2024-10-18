
"""Поиск элемента в списке, бинарным способом"""
def binary_search(lst, search_item):
    left_position = 0
    right_position = len(lst) - 1
    flag = False
    
    while left_position <= right_position and not flag:
        middle_elem = (left_position + right_position) // 2
        elem_list = lst[middle_elem]
        if elem_list == search_item:
            flag = True
            return flag
        if elem_list > search_item:
            right_position = middle_elem - 1 
        else:
            left_position = middle_elem + 1
    return flag
    

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst_sort = sorted(set(l)) 
item = 3
print(binary_search(lst_sort, item))








