"""Значимый подвиг 7. (Для закрепления предыдущего материала). Объявите функцию с именем str_min, которая сравнивает две переданные 
строки и возвращает минимальную из них (то есть, выполняется лексикографическое сравнение строк). Затем, используя функциональный 
подход к программированию (то есть, более сложные функции реализуются путем вызова более простых), реализовать еще две аналогичные функции:

- с именем str_min3 для поиска минимальной строки из трех переданных строк;
- с именем str_min4 для поиска минимальной строки из четырех переданных строк.

Выполнять функции не нужно, только записать.
"""


def str_min(a: str, b: str) -> str:
    """сравнивает две переданные строки и возвращает минимальную из них

    Args:
        a (str): _description_
        b (str): _description_

    Returns:
        str: _description_
    """
    
    return min(a, b)


def str_min3(a: str, b: str, c: str) -> str:
    """для поиска минимальной строки из трех переданных строк

    Args:
        a (str): _description_
        b (str): _description_

    Returns:
        str: _description_
    """
    return str_min(a, str_min(b, c))
    

def str_min4(a: str, b: str, c: str, d: str) -> str:
    """для поиска минимальной строки из четырех переданных строк

    Args:
        a (str): _description_
        b (str): _description_

    Returns:
        str: _description_
    """
    return str_min(a, str_min3(b, c, d))

a = 'т'
b = 'д'
c = 'е'
d = 'а'
print(str_min(a, b))
print(str_min3(a, b, c))
print(str_min4(a, b, c, d))

print(('yes','no')[False])

*x, e = (1, 2, 3, 4)

print('Function range: ', *range(5))

d = {0: "безнадежно", 1: "убого", 2: "неуд.", 3: "удовл.", 4: "хорошо", 5: "отлично"}
c = {44: "Good", 15: "Yes",}
print(*d.values())
print(*d.items())
v = {**d, **c}
print(v)
