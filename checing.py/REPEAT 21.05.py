'''
Подвиг 3. Для последовательной обработки файлов из некоторого списка, например:

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
Необходимо объявить класс ImageFileAcceptor, который бы выделял только файлы с указанными расширениями.

Для этого предполагается создавать объекты класса командой:

acceptor = ImageFileAcceptor(extensions)
где extensions - кортеж с допустимыми расширениями файлов, например: extensions = ('jpg', 'bmp', 'jpeg').

А, затем, использовать объект acceptor в стандартной функции filter языка Python следующим образом:

image_filenames = filter(acceptor, filenames)
Пример использования класса (эти строчки в программе писать не нужно):

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
P.S. Ваша задача только объявить класс ImageFileAcceptor. На экран ничего выводить не нужно. 
'''

from typing import Any


class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions
        
    def __call__(self, name, *args, **kwds):
        start= name.rfind('.')
        ext = '' if start == -1 else name[start+1:]
        return ext in self.extensions
        



filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames) # передается в виде функции
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]