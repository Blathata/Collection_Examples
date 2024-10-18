
class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = [3, 6, 8, 3, 7, 9, 45]

  
head_obj = ListObject(lst_in[0])
obj = head_obj

for i in range(1, len(lst_in)):
    new_obj = ListObject(lst_in[i])
    obj.link(new_obj)
    obj = new_obj
