class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right =None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True
        if value < node.data:
            if node.left:
                return self.__find(self, node.left, node, value)
            
        if value > node.data:
            if node.right:
                return self.__find(self, node.right, node, value)
            
        return node, parent, False # значит не нашли  вершину со значением value


    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        
        s, p, fl_find = self.__find(self.root, None, obj.data) #None родительская вершина для корня

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj
    
    def show_tree(self, node):
        """Отображает бинарное дерево"""
        if node is None:
            return
        
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

v = [10, 5, 7, 16, 13, 2, 20]

t = Tree()
for x in v:
    t.append(Node(x))


t.show_tree(t.root)

        
