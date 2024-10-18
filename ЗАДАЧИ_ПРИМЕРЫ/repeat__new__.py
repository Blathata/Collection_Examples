"""Наследование от отногоь класса __new__"""
class Singleton:
    _instance = None
    _instance_base = None
    
    
    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base
                   
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

class Game(Singleton):
    def __init__(self, name):
        if "name" not in self.__dict__:
            self.name = name
            
class Game2(Singleton):
    def __init__(self, name):
        if "name" not in self.__dict__:
            self.name = name


a = Singleton()
g = Game2('game1')
g2 = Game('game2')
print(id(g))
print(id(g2))
print(id(a))
print(g)

