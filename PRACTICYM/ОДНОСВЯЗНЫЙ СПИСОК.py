class StackObj:
    """для управления односвязным списком"""

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__data
    
    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj


class Stack:
    """для описания объектов односвязного списка"""
    def __init__(self):
        self.top = None # reference to the first object in the list
        self.last = None # referrnce to the last object in the list
    
    def push(self, obj):
        """добавление объекта класса StackObj в конец односвязного списка"""
        if self.last:
            self.last.next = obj
        
        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        """извлечение последнего объекта с его удалением из односвязного списка"""
        h = self.top
        if h is None:
            return
        while h.next != self.last:
            h = h.next
        if h:
            h.next = None
        last = self.last
        self.last = h
        if self.last is None:
            self.top = None

        return last
    
    def get_data(self):
        """получение списка из объектов односвязного списка"""
        s = []
        h = self.top
        while h:
            s.append(h.data)
            h = h.next
        return s
    
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']




    

        



             






