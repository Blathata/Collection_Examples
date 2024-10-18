s = sum(filter(lambda x: isinstance(x, int), data))

s = sum(filter(lambda x: type(x) is int, data))

isinstance(a, (int, float))

type(x) is int

type(b) in (bool, float, str)

type(b) == bool

return sum(i if type(i) is int else 0 for i in it)

if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))): # проверка на True через all

#------------------------------------------------------------------
"""Вхождение и невхождение в список с возвратом значеия"""

l_1 = [1, 2, 3, 4]
l_2 = [1, 2, 5, 7]

# различия списков
list_1 = list(set(l_1).difference(l_2))

# совпадения  
list_2 = list(set(l_1).intersection(l_2))

print(list_1)
print(list_2)
#------------------------------------------------------------------

#проверка на вхождение если есть хоть один символ невходящий в CHARS_CORRECT
CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits
if not set(name) < set(cls.CHARS_CORRECT):
    raise ValueError("некорректное поле name")

#------------------------------------------------------------------

# множество x  входит в set_chars
s = name.split() # "SERGEI BALAKIREV"
set_chars = set(cls.CHARS_FOR_NAME) # CHARS_FOR_NAME = ascii_lowercase.upper() + digits
return all(map(lambda x: set(x) < set_chars, s)) # set(x) проверяет есть ли лишний символ, если нет в set_chars
