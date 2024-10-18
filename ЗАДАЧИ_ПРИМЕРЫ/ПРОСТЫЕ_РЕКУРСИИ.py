"""
Простые примеры написания рекурсии, сумма всех чисел 
и строка наоботрот.

Частые ошибки:
- нет условия выхода (base case)
- нет return в одной из веток
- нет уменьшения данных
"""

def my_sum(a_lst: list) -> int:
    if not a_lst:
        return 0
    if len(a_lst) == 1:
        return a_lst[0]
    return a_lst[0] + my_sum(a_lst[1:])


def my_reverse(a_str: str) -> str:
    if not a_str:
        return ''
    if len(a_str) == 1:
        return a_str
    return my_reverse(a_str[1:]) + a_str[0]


if __name__ =="__main__":
    assert my_sum([]) == 0
    assert my_sum([1]) == 1
    assert my_sum([-1]) == -1
    assert my_sum([2,2]) == 4
    print(my_sum([1, 2, 3, 5]))


if __name__ == '__main__':
    assert my_reverse('') == ''
    assert my_reverse('a') == 'a'
    assert my_reverse('10') == '01'
    assert my_reverse('hello') == 'olleh'
    print(my_reverse('Hello'))