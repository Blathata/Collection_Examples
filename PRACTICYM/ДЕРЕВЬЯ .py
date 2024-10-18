class TreeObj:
    """для описания вершин и листьев решающего дерева"""

    def __init__(self, indx: int, value: str = None):
        """
        indx - проверяемый в вершине дерева индекс вектора x
        value - значение, хранящееся в вершине 
        __left - ссылка на следующий объект дерева по левой ветви
        __right - ссылка на следующий объект дерева по правой ветви

        Для работы с локальными приватными атрибутами __left и __right необходимо объявить объекты-свойства с именами left и right.
        """
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None


class DecisionTree:
    """для работы с решающим деревом в целом"""
    
    @classmethod
    def predict(cls, root, x):
        """для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root (возвращает значение узла - атрибут value)"""
        pass

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """для добавления вершин в решающее дерево (метод должен возвращать 
        добавленную вершину - объект класса TreeObj)
        
        obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
        node - ссылка на объект дерева, к которому присоединяется вершина obj;
        left - флаг, определяющий ветвь дерева (объекта node), к которой присоединяется объект obj (True - к левой ветви; False - к правой).
        """
        pass

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом


