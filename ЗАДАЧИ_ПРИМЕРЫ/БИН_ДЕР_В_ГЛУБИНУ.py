def show_tree(self, node):
    if node is None:
        return
 
    self.show_tree(node.left)
    print(node.data)
    self.show_tree(node.right)

show_tree(root)

