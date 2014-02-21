class Node():#similar to linkedlists find the position in reference to neighbouring nodes
    left=None
    right=None
    parent=None
    value=None
    def __init__(self, value):
        self.value=value#sets the value of the node
    def set_parent(self, parent):
        self.parent=parent#adds the relationship/edge
    def add_left(self, node):
        node.set_parent(self)
        self.left=node
    def add_right(self, node):
        self.right=node
        node.set_parent(self)
    def add_node(self, node):
        if node.value<self.value:
            if self.left==None:
               self.add_left(node)
            else:
                self.left.add_node(node)
        else: 
            if self.right==None:
               self.add_right(node)
            else:
                self.right.add_node(node)#sets up the links, lowest value is always on the left

