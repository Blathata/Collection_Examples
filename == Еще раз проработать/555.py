class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls._instance_base == None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base
            
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


class Game(Singleton):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


s = Singleton()

a = Game('Игра')
b = Game('Игра2')

print(id(s))
print(id(a))

print(s)
print(a.name)
print(b.name)


