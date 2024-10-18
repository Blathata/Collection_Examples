menu = {**menu, **dict([i.split('=') for i in lst_in])}

if type(path[f]) == dict: # type check
    
n = list(map(lambda x: ('-', x)[len(x)>5], input().split())) #

# преобразование списка в словарь с заменой 
lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']

d = {int[b] : a for a, b in [i.split(':') for i in lst_in]}

return sum(filter(lambda x: type(x) is int and x % 2 ==0, it), 0)

elements = [(Line, Rect, Ellipse)[randint(0,2)](1, 2, 3, 4)for _ in range(0,127)] # выбор класса случайным образом в цикле







# надо разобрать
def get_add(a, b):
    if  {type(a), type(b)} in ({str}, {int}, {float}, {int, float}):
        return a + b
    
def get_add(a, b):
    tset = {type(a), type(b)}
    if tset <= {int, float} or tset == {str}:
        return a + b